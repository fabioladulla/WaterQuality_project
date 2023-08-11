def plot_continuous_in_boxplot(df: pd.DataFrame):
    '''
    Plot continuous variables of a dataframe in histogram and boxplot
    '''
    import matplotlib.pyplot as plt
    import seaborn as sns

    for column in df.columns:
        fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})
        sns.boxplot(data=df, x=column, ax=ax_box)
        sns.histplot(data=df, x=column, ax=ax_hist)
        plt.show()


def plot_importance(model, features, num=None, save=False):
    if num is None:
        num = len(features)
        
    feature_imp = pd.DataFrame({'Value': model.feature_importances_, 'Feature': features.columns})
    plt.figure(figsize=(9, 7))
    sns.set(font_scale=1)
    custom_palette = sns.color_palette("Paired", 9)
    sns.barplot(x="Value", y="Feature", data=feature_imp.sort_values(by="Value", ascending=False)[0:num], palette=custom_palette)
    plt.title('Features')
    plt.tight_layout()
    
    if save:
        plt.savefig('../Images/feature_rank.png')
    
    plt.show()