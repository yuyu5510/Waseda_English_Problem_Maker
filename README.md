# Waseda_English_Problem_Maker
早稲田大学理系入試の英語の大問5を半自動生成するやつです。定義と例文が英文で出され、正解の単語を選ぶ問題です。ただし、選択肢は最初の一文字以外の文字は[a,b,c,d,e,f,g]ならば１、[h,i,j,k,l,m]ならば2,[n,o,p,q,r,s]ならば3,[t,u,v,w,x,y,z]ならば4というように数字に置換されています。

nltkのダウンロードが必要です。
nltkのダウンロードはターミナルで`pip install nltk`を打った後、`nltk.download('all')`を打てばダウンロードできます。

今回、定義や例文を引っ張り出すためのnltk.wordnetでは単語によっては登録されている定義や例文がなく、期待通りの動作をしない欠陥があります。ご了承ください。
