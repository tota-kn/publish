# vim remapの種類と特徴
1. Normal modeリマップ（:nnoremap）：    
    - これはNormalモードでのキー操作をリマップするためのコマンドです。
    - `:nnoremap {lhs} {rhs}`の形式で使用します。{lhs}は置き換えるキー操作、{rhs}はリマップ先のキー操作です。
    - 他のモード（InsertモードやVisualモードなど）ではリマップが有効になりません。
    - `nore`は「再帰的なリマップを無効化する」という意味です。通常、再帰的なリマップは有効ですが、`nore`を使用することで無効化できます。
2. Insert modeリマップ（:inoremap）：
    
    - これはInsertモードでのキー操作をリマップするためのコマンドです。
    - `:inoremap {lhs} {rhs}`の形式で使用します。
    - NormalモードやVisualモードではリマップが有効になりません。
3. Visual modeリマップ（:vnoremap）：
    
    - これはVisualモードでのキー操作をリマップするためのコマンドです。
    - `:vnoremap {lhs} {rhs}`の形式で使用します。
    - NormalモードやInsertモードではリマップが有効になりません。
4. コマンドラインモードリマップ（:cnoremap）：
    
    - これはコマンドラインモード（コマンドを入力するモード）でのキー操作をリマップするためのコマンドです。
    - `:cnoremap {lhs} {rhs}`の形式で使用します。
    - NormalモードやInsertモード、Visualモードではリマップが有効になりません。
