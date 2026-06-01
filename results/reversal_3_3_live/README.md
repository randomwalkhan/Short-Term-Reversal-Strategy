# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 14:55:05 EDT`
Last processed slot: `entry_1500`

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
  AAPL           92.31               13            1.43              3.13        310.72                17.18         0.524            pass              0.510             36.4                           0.427                2.45              0.461                                 ok            True                  False
  INSM           67.86               28            1.80              1.34        106.33               110.85         0.735            pass              0.353             53.2                           0.547               -3.80             -0.191                                 ok           False                  False
   WMT           78.57               14            1.30              1.06        115.30                32.67         0.559            pass              0.176             31.1                           0.328              -13.09             -1.683 downtrend_blocked_slope_and_streak           False                  False
  REGN           72.73               11            2.09              9.00        610.92                42.14         0.558            pass              0.076              4.6                           0.234              -13.67             -0.858 downtrend_blocked_slope_and_streak           False                  False
   AEP           60.00                5            1.70              1.51        126.02                24.34         0.546            pass              0.116             20.3                           0.401               -0.51             -0.058                                 ok           False                  False
   PEP           91.67               12            1.55              1.56        143.52                22.18         0.535            pass              0.426             16.2                           0.265               -4.80             -0.458            downtrend_blocked_slope           False                  False
  AMGN           80.00                5            2.03              4.78        334.74                25.52         0.533            pass              0.157             34.6                           0.594                1.12              0.254                                 ok           False                  False
  COST           60.00               10            1.32              8.84        952.53                27.93         0.532            pass              0.162             36.3                           0.345              -10.03             -1.335 downtrend_blocked_slope_and_streak           False                  False
  ISRG           81.82               11            2.64              7.83        421.28                37.20         0.507            pass              0.144             12.8                           0.135               -1.82             -0.460 downtrend_blocked_slope_and_streak           False                  False
  ROST           50.00                2            3.37              5.47        229.39                40.27         0.498 below_threshold              0.061              3.8                           0.213                5.25              0.949                                 ok           False                  False
   APP           84.44               45            0.09              0.40        612.92                70.19         0.482 below_threshold              0.661             98.0                           0.635               22.26              2.685                                 ok           False                  False
 GOOGL           90.62               32            0.72              1.92        379.52                25.94         0.482 below_threshold              0.657             59.7                           0.692               -4.84             -0.361            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                detail
2026-06-01T14:55:05.958850-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T14:50:06.115038-04:00       entry_1500  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T14:50:06.115038-04:00       entry_1500 timing_overlay                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-01", "training_samples": 5165, "window": 5}
2026-06-01T12:50:07.149920-04:00      manage_1300           exit {"asset_type": "option", "contract_symbol": "SNPS260717C00470000", "fill_price": 42.3, "pnl": 2820.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 20.0, "ticker": "SNPS"}
2026-06-01T12:00:03.957402-04:00 early_entry_1200  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:55:05.058620-04:00 early_entry_1155  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:50:02.013615-04:00 early_entry_1150  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:45:04.960036-04:00 early_entry_1145  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:40:03.918897-04:00 early_entry_1140  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:35:04.962377-04:00 early_entry_1135  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601145505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601145505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601145505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601145505)

</details>
