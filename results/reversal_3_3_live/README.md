# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 11:35:01 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$14,107.75`
- Equity: `$28,037.75`
- Realized PnL: `$16,462.75`
- Unrealized PnL: `$1,575.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  FTNT     option         option FTNT260717C00125000       2026-05-20                   0     14     12355.0                 13930.0         8.82           9.95      126.75        128.79          bid_ask_mid                       9.95                bid_ask_mid                    True          1575.0                  12.75         100.0               38              0.69         41.39           40.43                  70.74                1300.0           40.0               0.12                      ok
```

## Today's Closed Trades (2026-05-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           92.86               28            0.72              1.53        301.65                69.06         0.634            pass              0.771             81.6                           0.443                3.69              0.564                                 ok            True                  False
   WMT           92.86               14            1.16              1.09        133.73                20.68         0.530            pass              0.619             65.6                           0.653                2.16              0.343                                 ok            True                  False
 GOOGL           86.67               30            0.82              2.21        386.71                41.27         0.517            pass              0.464             33.6                           0.306               -3.40             -0.210                                 ok            True                  False
  CTSH           88.89               27            1.10              0.39         50.71                50.98         0.507            pass              0.615             71.4                           0.694               -1.28             -0.216                                 ok            True                  False
  TMUS           81.25               16            1.99              2.69        192.27                36.70         0.505            pass              0.176             17.5                           0.375               -1.86             -0.221                                 ok            True                  False
  TEAM           88.24               34            1.89              1.15         86.13               114.61         0.612            pass              0.629             62.9                           0.583               -4.30             -0.541 downtrend_blocked_slope_and_streak           False                  False
  PAYX           95.24               21            0.33              0.22         94.39                29.36         0.559            pass              0.798             89.5                           0.690                4.37              0.241                                 ok           False                  False
  GOOG           85.71               28            0.87              2.35        383.89                41.08         0.514            pass              0.418             31.4                           0.283               -3.44             -0.222           downtrend_blocked_streak           False                  False
  ADSK           88.46               26            1.10              1.88        243.36                38.52         0.497 below_threshold              0.609             75.6                           0.712               -0.66             -0.142                                 ok           False                  False
  SNPS           97.44               39            0.20              0.69        493.57                41.71         0.495 below_threshold              0.928             95.1                           0.699               -2.29             -0.339 downtrend_blocked_slope_and_streak           False                  False
   KDP           90.00               40            0.05              0.01         28.85                34.80         0.493 below_threshold              0.807             97.1                           0.760                0.96              0.153                                 ok           False                  False
   TRI           75.00               12            2.66              1.62         86.65                57.28         0.482 below_threshold              0.193             43.8                           0.308               -7.32             -0.903 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-20T11:35:01.033169-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:30:01.977277-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:25:06.020090-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:20:04.061677-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:15:01.033814-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:10:02.083171-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:05:01.079772-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:00:03.973296-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T10:55:04.047991-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T10:50:01.057025-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520113501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520113501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520113501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520113501)

</details>
