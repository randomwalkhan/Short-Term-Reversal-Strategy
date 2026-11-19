# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-19 10:30:04 EST`
Last processed slot: `manage_1030`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$100,946.30`
- Equity: `$100,946.30`
- Realized PnL: `$90,946.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-19)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00400000     15          2026-11-18         2026-11-19        33.15      29.835 -4972.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   APP           94.74               19            2.77              7.57        387.67               121.61         0.776          pass              0.533              0.7                           0.084                6.74              0.317                  ok            True                  False
  IDXX           97.14               35            0.85              4.14        696.70                78.12         0.695          pass              0.777             46.8                           0.555                3.26              0.213                  ok            True                  False
  ABNB           80.95               21            1.65              2.08        179.32                55.20         0.579          pass              0.177              6.9                           0.186                4.17             -0.123                  ok            True                  False
 CMCSA           92.86               14            1.58              0.28         25.12                34.19         0.564          pass              0.495             23.1                           0.285               -0.44              0.259                  ok            True                  False
  REGN           81.82               33            0.91              6.03        942.95                54.27         0.563          pass              0.438             59.9                           0.705                3.77              0.507                  ok            True                  False
  AAPL          100.00               19            1.08              2.65        351.31                27.20         0.552          pass              0.532              5.5                           0.148                1.38              0.208                  ok            True                  False
  ODFL           83.33               24            1.30              1.60        174.42                43.99         0.551          pass              0.279             13.8                           0.200                1.33              0.381                  ok            True                  False
  COST           86.96               23            0.55              4.24       1094.80                23.52         0.538          pass              0.482             52.0                           0.566                2.34              0.456                  ok            True                  False
  FAST           93.33               15            1.06              0.40         53.79                20.11         0.536          pass              0.502             19.7                           0.287                0.93              0.101                  ok            True                  False
  VRSK           80.00               20            1.83              2.59        201.20                47.31         0.533          pass              0.187             22.4                           0.338               -6.08             -0.178                  ok            True                  False
   HON           81.48               27            0.74              1.15        222.21                33.05         0.522          pass              0.240             11.8                           0.132                2.76             -0.031                  ok            True                  False
  GEHC           81.25               32            0.86              0.50         83.44                39.18         0.515          pass              0.322             30.1                           0.343               -0.97             -0.071                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                           detail
2026-11-19T10:30:04.546056-05:00 early_entry_1030 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:25:05.944079-05:00 early_entry_1025 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:20:05.689332-05:00 early_entry_1020 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:20:05.689332-05:00      manage_1030               exit {"asset_type": "option", "contract_symbol": "APP270115C00400000", "fill_price": 29.835, "pnl": -4972.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "APP"}
2026-11-19T10:15:01.694448-05:00 early_entry_1015 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:10:05.743746-05:00 early_entry_1010 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:05:05.527736-05:00 early_entry_1005 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:00:06.381004-05:00 early_entry_1000 early_entry_shadow                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T00:00:05.435730-05:00     data_refresh       data_refresh                                                                                                                                                        {'saved': 91, 'empty': 2}
2026-11-18T15:10:05.947802-05:00       entry_1500       slot_skipped                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261119103004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261119103004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261119103004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261119103004)

</details>
