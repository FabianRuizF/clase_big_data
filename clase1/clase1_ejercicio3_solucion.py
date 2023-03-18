
def filter_word(word):
  if ("a" in word):
    return ""
  if ("e" in word):
    return ""
  if (word in BAN_LIST):
    return ""
  return word

df["filtered_word"] = df["word"].apply(filter_word)
len(df[df.filtered_word==""])
