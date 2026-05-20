# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 11:30:01 EDT`
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
- Equity: `$28,002.75`
- Realized PnL: `$16,462.75`
- Unrealized PnL: `$1,540.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  FTNT     option         option FTNT260717C00125000       2026-05-20                   0     14     12355.0                 13895.0         8.82           9.93      126.75         128.4          bid_ask_mid                       9.93                bid_ask_mid                    True          1540.0                  12.46         100.0               38              0.69         41.39           41.62                  70.74                1300.0           40.0               0.12                      ok
```

## Today's Closed Trades (2026-05-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           93.33               30            0.69              1.46        301.69                69.06         0.624            pass              0.799             82.5                           0.474                3.73              0.566                                 ok            True                  False
   WMT           92.86               14            1.25              1.18        133.70                20.68         0.524            pass              0.611             62.9                           0.655                2.07              0.339                                 ok            True                  False
 GOOGL           86.21               29            0.89              2.41        386.63                41.27         0.519            pass              0.427             27.6                           0.298               -3.47             -0.213                                 ok            True                  False
  CTSH           87.50               24            1.23              0.44         50.69                50.98         0.517            pass              0.549             68.0                           0.675               -1.40             -0.222                                 ok            True                  False
  ADSK           86.96               23            1.21              2.07        243.27                38.52         0.508            pass              0.542             73.1                           0.678               -0.77             -0.147                                 ok            True                  False
  TMUS           80.00               15            2.10              2.85        192.20                36.70         0.502            pass              0.122             12.8                           0.274               -1.97             -0.226                                 ok            True                  False
  TEAM           88.57               35            1.72              1.04         86.17               114.61         0.617            pass              0.656             66.3                           0.646               -4.13             -0.533 downtrend_blocked_slope_and_streak           False                  False
  PAYX           95.24               21            0.33              0.22         94.39                29.36         0.559            pass              0.798             89.7                           0.700                4.38              0.241                                 ok           False                  False
  GOOG           85.71               28            0.95              2.57        383.80                41.08         0.509            pass              0.398             24.9                           0.262               -3.52             -0.225           downtrend_blocked_streak           False                  False
   KDP           90.00               40            0.07              0.01         28.84                34.80         0.492 below_threshold              0.804             96.2                           0.735                0.95              0.152                                 ok           False                  False
  SNPS           97.37               38            0.39              1.36        493.29                41.71         0.488 below_threshold              0.906             90.3                           0.718               -2.48             -0.348 downtrend_blocked_slope_and_streak           False                  False
   TRI           75.00               12            2.59              1.58         86.67                57.28         0.487 below_threshold              0.198             45.2                           0.289               -7.26             -0.900 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-20T11:30:01.977277-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:25:06.020090-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:20:04.061677-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:15:01.033814-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:10:02.083171-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:05:01.079772-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:00:03.973296-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T10:55:04.047991-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T10:50:01.057025-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T10:45:05.974600-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520113001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520113001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520113001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520113001)

</details>
