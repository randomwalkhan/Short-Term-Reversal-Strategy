# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 13:45:04 EDT`
Last processed slot: `manual`

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
   HON           84.21               19            0.93              1.55        237.20                24.41         0.522            pass              0.396             57.1                           0.741               10.51              1.123                                 ok            True                  False
  AAPL           93.33               15            1.37              2.99        310.78                17.18         0.515            pass              0.558             39.3                           0.587                2.52              0.464                                 ok            True                  False
  INSM           46.15               13            3.57              2.67        105.76               110.85         0.698            pass              0.111              6.9                           0.253               -5.54             -0.274            downtrend_blocked_slope           False                  False
   WMT           76.92               13            1.36              1.10        115.28                32.67         0.561            pass              0.161             28.3                           0.515              -13.14             -1.685 downtrend_blocked_slope_and_streak           False                  False
  REGN           78.57               14            1.90              8.17        611.28                42.14         0.557            pass              0.118             12.0                           0.304              -13.50             -0.849 downtrend_blocked_slope_and_streak           False                  False
  COST           63.64               11            1.22              8.13        952.83                27.93         0.536            pass              0.184             41.3                           0.587               -9.94             -1.330 downtrend_blocked_slope_and_streak           False                  False
   AEP           60.00                5            1.86              1.65        125.96                24.34         0.536            pass              0.092             12.8                           0.310               -0.67             -0.065                                 ok           False                  False
  ROST           66.67                3            3.15              5.11        229.54                40.27         0.525            pass              0.081              9.4                           0.374                5.49              0.959                                 ok           False                  False
   PEP           86.67               15            1.36              1.37        143.60                22.18         0.521            pass              0.343             26.5                           0.458               -4.62             -0.449            downtrend_blocked_slope           False                  False
  ISRG           82.61               23            1.55              4.61        422.66                37.20         0.496 below_threshold              0.352             48.6                           0.352               -0.73             -0.409                                 ok           False                  False
  AMZN          100.00                2            3.24              6.15        268.01                21.29         0.488 below_threshold              0.484             11.7                           0.383               -0.86              0.225                                 ok           False                  False
   EXC           60.00               10            1.94              0.62         45.37                21.39         0.486 below_threshold              0.093             14.9                           0.345                3.17              0.402                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601134504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601134504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601134504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601134504)

</details>
