import pandas as pd

def unite_col(input_df, unite_by, pattern="", united_col_name="untitled", output_json=False):
    input_df[united_col_name] = input_df[unite_by].apply(lambda x: pattern.join(x.map(str)), axis=1)
    if(output_json):
        output = input_df.to_dict("records")
    else:
        output = input_df
    return output

def separate_col(input_df, sep_by, pattern="", sep_to_names=None, output_json=False):
    if(sep_to_names==None):
        split_cols = input_df[sep_by].str.split(pattern,expand=True)
        names_split = split_cols.columns
        input_df[names_split]=split_cols
    else:
        input_df[sep_to_names] = input_df[sep_by].str.split(pattern,expand=True)
       
    if(output_json):
        output = input_df.to_dict("records")
    else:
        output = input_df
    return output

def groupby_col(input_data, group_by, summmarize_at = None, operator = "count", output_json = False):
    
    """group by and summarize data frame"""
    """operator: mean, sum, min, max, median, unique (unique will return unique values in a list format), count, nunique"""
    if (summmarize_at == None):
        output_df = pd.DataFrame( input_data.groupby(group_by).count().reset_index() )
    else:
        if(operator == "mean"):
            output_df = pd.DataFrame( input_data.groupby(group_by)[summmarize_at].mean().reset_index() )
        elif(operator == "sum"):
            output_df = pd.DataFrame( input_data.groupby(group_by)[summmarize_at].sum().reset_index() )
        elif(operator == "min"):
            output_df = pd.DataFrame( input_data.groupby(group_by)[summmarize_at].min().reset_index() )
        elif(operator == "max"):
            output_df = pd.DataFrame( input_data.groupby(group_by)[summmarize_at].max().reset_index() )
        elif(operator == "median"):
            output_df = pd.DataFrame( input_data.groupby(group_by)[summmarize_at].median().reset_index() )
        elif(operator == "unique"):
            output_df = pd.DataFrame( input_data.groupby(group_by)[summmarize_at].unique().reset_index() )
        elif(operator == "count"):
            output_df = pd.DataFrame( input_data.groupby(group_by)[summmarize_at].count().reset_index() )
        elif(operator == "nunique"):
            output_df = pd.DataFrame( input_data.groupby(group_by)[summmarize_at].nunique().reset_index() )
        else:
            print("Hmm... operator should be one of mean, sum, min, max, median, unique, count, nunique!")
            
    if(output_json):
        output = output_df.to_dict("records")
    else:
        output = output_df
        
    return output      


def groupby_across(input_data, group_by, summmarize_at, operation=None, output_json = False):
    if(operation==None):
        df_grouped = input_data.groupby(group_by).agg({summmarize_at:["min", "max", "sum", "median"]})
        df_grouped.columns = ["_".join(x) for x in df_grouped.columns.ravel()]
    else:
        df_grouped = input_data.groupby(group_by).agg({summmarize_at: operation})
        df_grouped.columns = ["_".join(x) for x in df_grouped.columns.ravel()]
    
    df_grouped = pd.DataFrame(df_grouped.reset_index() )
    if(output_json):
        output = df_grouped.to_dict("records")
    else:
        output = df_grouped
        
    return output     

def pivot_tb(input_data, group_by, summmarize_at, operation="count", output_json = False, na_fill=0):
    all_groups = group_by + [summmarize_at]

    df_grouped = input_data.groupby(all_groups).agg({summmarize_at:[operation]})
    df_grouped.columns = ["_".join(x) for x in df_grouped.columns.ravel()]
    df_grouped=df_grouped.reset_index()
    pivot_value = summmarize_at + "_" + operation
    result = pd.pivot_table(df_grouped,index=group_by, columns=summmarize_at, values=pivot_value).fillna(na_fill)
    output_df = result.reset_index()
    output_df.columns.name = None
    
    if(output_json):
        output = output_df.to_dict("records")
    else:
        output = output_df
        
    return output    

def pivot_rate(input_data, group_by, summmarize_at, output_json = False, na_fill=0):
    all_groups = group_by + [summmarize_at]
    df_grouped = input_data.groupby(all_groups).agg({summmarize_at:["count"]})
    df_grouped.columns = ["_".join(x) for x in df_grouped.columns.ravel()]
    df_grouped=df_grouped.reset_index()
    total_ct_df = df_grouped.groupby(group_by).agg(sum)
    pivot_count = summmarize_at + "_count" 
    pivot_total = summmarize_at + "_total" 
    pivot_perc = summmarize_at + "_perc" 
    total_ct_df=total_ct_df.rename(columns={pivot_count: pivot_total})

    df_grouped=pd.merge(df_grouped,total_ct_df,on=group_by ,how='left')

    df_grouped[pivot_perc]=(df_grouped[pivot_count]/df_grouped[pivot_total])*100
    df_grouped=df_grouped.drop(pivot_total, axis=1)
    result = pd.pivot_table(df_grouped,index=group_by, columns=summmarize_at).fillna(na_fill)
    result.columns.name = None
    result.columns = ["_".join(x) for x in result.columns.ravel()]
    output_df = result.reset_index()
    output_df.columns.name = None
    
    if(output_json):
        output = output_df.to_dict("records")
    else:
        output = output_df
        
    return output 

def simplify_network_df(df, from_col = "from", to_col = "to", keep = "first"):
    """simplify the network dataframe from directed to undirected"""
    temp_new_col_name = from_col+to_col+'merged'
    df[temp_new_col_name] = df[[from_col, to_col]].apply(lambda x: list(x), axis=1)
    df[temp_new_col_name] = df[[temp_new_col_name]].apply(lambda x: str(sorted(x[0]) ), axis=1)
    df = df.drop_duplicates(subset=[temp_new_col_name], keep=keep)
    output_df = df.drop([temp_new_col_name], axis = 1)
   
    return output_df