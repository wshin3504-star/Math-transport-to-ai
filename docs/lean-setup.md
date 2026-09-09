# Lean 4 安装指引（Windows，本周 Day 3–4 执行）

> Phase 0 的 Lean 目标是「能读懂、能玩 NNG」，安装 10 分钟即可，不必折腾工具链。

## 1. 安装 elan（Lean 版本管理器）

下载并运行官方安装器：

- 地址：<https://elan.lean-lang.org/elan-init.exe>
- 双击运行，一路默认（安装到 `%USERPROFILE%\.elan`，会自动加 PATH）
- 装完**重开终端**，验证：

```powershell
elan --version
lake --version
lean --version
```

## 2. VS Code 配置

1. 安装 VS Code（如未装）：<https://code.visualstudio.com/>
2. 扩展商店搜 `lean4`（发布者 leanprover），安装官方扩展
3. 新建任意 `.lean` 文件，右下角出现 `Lean 4` 且无报错即成功

## 3. 建第一个练习项目（可选，Day 5+）

```powershell
cd C:\Users\32752\Desktop\转码参考\Transport_to_AI\lean
lake init playground   # 生成 playground 目录
cd playground
code .                 # VS Code 打开，编辑 Main.lean 试试
```

## 4. 学习路线（Phase 0 内）

| 顺序 | 资源 | 形式 | 出口标准 |
|---|---|---|---|
| 1 | Natural Number Game <https://adam.math.hhu.de/> | 网页，**免安装** | 全部关卡通关，截图存 lean/ 目录 |
| 2 | Mathematics in Lean | 在线书 + 本地 lake 项目 | 完成 ch2（逻辑）与 ch3（集合）练习 |
| 3 | Functional Programming in Lean | 在线书 | 选读，为读 LeanDojo 代码打底 |

> 注意：Natural Number Game 直接浏览器玩即可，**不要等本地环境**。
> 每天固定 30 分钟，用「番茄钟 + 每关 commit 一条进度」的节奏。

## 5. 常见问题

- 终端找不到 elan：重开终端 / 手动把 `%USERPROFILE%\.elan\bin` 加入 PATH
- VS Code 里 Lean 卡在 downloading：首次下载 Mathlib 依赖较慢，挂后台
- NNG 某关卡死：Lean Zulip 社区 <https://leanprover.zulipchat.com/> 搜关卡号，
  该社区对新人非常友好，直接英文提问即可
