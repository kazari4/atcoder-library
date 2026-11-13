# AtCoder Python Library

Obsidian Vault 内で管理する、AtCoder 提出用の Python ライブラリです。ユーザーが指定したアルゴリズムだけ追加します。

## ライブラリ一覧

| アルゴリズム | 実装（GitHub） | ローカル実装 | 対応する Obsidian ノート |
| --- | --- | --- | --- |
| Rolling Hash | [Strings/rolling_hash.py](https://github.com/kazari4/atcoder-library/blob/main/Strings/rolling_hash.py) | [Strings/rolling_hash.py](Strings/rolling_hash.py) | [Rolling Hash](../Algorithms/Strings/Rolling%20Hash.md) |

## 使い方

実装は `Algorithms/` と同じジャンル別のディレクトリに配置します。空のディレクトリは Git に記録されないため、実装を追加する際に必要なジャンルを作成します。現在の実装は `Strings/rolling_hash.py` です。Obsidian のファイル一覧に `.py` が表示されない場合は、**設定 → ファイルとリンク → すべてのファイル拡張子を検出**をオンにしてください。

1. 一覧の GitHub リンクから実装を開き、必要なコードを AtCoder の提出欄へコピーします。
2. 実装ファイルは単体でコピーして動く形にし、Vault 内の別ファイルへの依存を持たせません。
3. 実装ファイルの先頭に、公開後の GitHub 上のファイル URL を Python コメントで記載します。URL を含めてファイル全体をコピーできます。

```python
# Source: https://github.com/kazari4/atcoder-library/blob/main/Strings/rolling_hash.py
```

公開済み実装への直接リンクを対応する Obsidian ノートにも掲載します。

## 公開

このディレクトリは独立した Git リポジトリです。GitHub の Public リポジトリ作成と push は、どちらも事前にユーザーの承認を得てから行います。
