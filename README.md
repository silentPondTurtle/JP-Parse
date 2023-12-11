- Breaks if the sentence contains numbers
- Potentially breaks if it contains English letters
- Also sometimes returns incorrect furigana due to MeCab. eg.) 私 -> わたし -> わたくし

Examples (original sentence on top, generated furigana sentence on bottom)
````
その人には二回会った。 
その人[ひと]には二[に]回[かい]会[あ]った。 

私は腕時計を四つ持っています。 
私[わたくし]は腕[うで]時計[とけい]を四[よん]つ持[も]っています。 

四月に大学に入学しました。 
四[よん]月[がつ]に大学[だいがく]に入学[にゅうがく]しました。 

ハワイは四回目です。 
ハワイは四[よん]回[かい]目[め]です。 
````
