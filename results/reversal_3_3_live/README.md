# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 13:20:04 EDT`
Last processed slot: `manage_1330`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$33,669.25`
- Equity: `$33,669.25`
- Realized PnL: `$23,669.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  MRVL     option         option MRVL260717C00200000      5          2026-06-01         2026-06-01        28.30       25.47 -1415.0       -10.0        stop_loss_hit_at_scan
  SNPS     option         option SNPS260717C00470000      4          2026-05-29         2026-06-01        35.25       42.30  2820.0        20.0 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           93.75               16            1.11              0.48         60.97                14.75         0.507            pass              0.590             44.3                           0.629                0.08              0.033                                 ok            True                  False
  INSM           46.15               13            3.52              2.64        105.78               110.85         0.702            pass              0.109              6.3                           0.275               -5.49             -0.272            downtrend_blocked_slope           False                  False
  CSCO           95.00               40            0.01              0.01        120.42                51.99         0.578            pass              0.957             99.6                           0.769                1.86              0.290                                 ok           False                  False
  REGN           81.25               16            1.80              7.76        611.46                42.14         0.553            pass              0.169             13.3                           0.318              -13.41             -0.844 downtrend_blocked_slope_and_streak           False                  False
   WMT           75.00               12            1.56              1.26        115.21                32.67         0.552            pass              0.122             17.8                           0.347              -13.31             -1.695 downtrend_blocked_slope_and_streak           False                  False
   AEP           60.00                5            1.68              1.49        126.03                24.34         0.548            pass              0.119             21.3                           0.347               -0.49             -0.057                                 ok           False                  False
   PEP           91.67               12            1.60              1.61        143.50                22.18         0.532            pass              0.418             13.5                           0.250               -4.85             -0.460            downtrend_blocked_slope           False                  False
   HON           78.57               14            1.23              2.04        236.98                24.41         0.531            pass              0.210             43.4                           0.677               10.18              1.109                                 ok           False                  False
  ROST           66.67                3            3.18              5.16        229.52                40.27         0.523            pass              0.078              8.6                           0.377                5.46              0.958                                 ok           False                  False
  AAPL           80.00                5            2.16              4.72        310.04                17.18         0.521            pass              0.064              4.1                           0.175                1.70              0.428                                 ok           False                  False
  COST           55.56                9            1.53             10.24        951.93                27.93         0.519            pass              0.130             26.2                           0.435              -10.22             -1.345 downtrend_blocked_slope_and_streak           False                  False
  ISRG           83.33               24            1.47              4.38        422.76                37.20         0.496 below_threshold              0.385             51.2                           0.433               -0.65             -0.406                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                detail
2026-06-01T12:50:07.149920-04:00      manage_1300          exit {"asset_type": "option", "contract_symbol": "SNPS260717C00470000", "fill_price": 42.3, "pnl": 2820.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 20.0, "ticker": "SNPS"}
2026-06-01T12:00:03.957402-04:00 early_entry_1200 entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:55:05.058620-04:00 early_entry_1155 entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:50:02.013615-04:00 early_entry_1150 entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:45:04.960036-04:00 early_entry_1145 entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:40:03.918897-04:00 early_entry_1140 entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:35:04.962377-04:00 early_entry_1135 entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:30:03.931988-04:00 early_entry_1130 entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:25:04.832152-04:00 early_entry_1125 entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:20:01.993474-04:00 early_entry_1120 entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601132004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601132004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601132004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601132004)

</details>
