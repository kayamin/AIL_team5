# 筋トレのカウント
## 半教師ありでやってみる
カメラで撮った画像にはラベルが付いているが、動画の方には付いていない  
→`sklearn.semi_supervised.LabelPropagation`を使う

## 特徴量設計
### 1. 腕周辺
肩を原点とした肘と手の座標  
→向きに寄らないように距離で定義してもいいかも

## 今後の目標
- [ ] どんな人の