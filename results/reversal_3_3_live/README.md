# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 11:20:04 EDT`
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
- Equity: `$27,757.75`
- Realized PnL: `$16,462.75`
- Unrealized PnL: `$1,295.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  FTNT     option         option FTNT260717C00125000       2026-05-20                   0     14     12355.0                 13650.0         8.82           9.75      126.75         128.2          bid_ask_mid                       9.75                bid_ask_mid                    True          1295.0                  10.48         100.0               38              0.69         41.39           41.32                  70.74                1300.0           40.0               0.12                      ok
```

## Today's Closed Trades (2026-05-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           90.91               11            1.33              1.25        133.67                20.68         0.537            pass              0.533             60.7                           0.603                1.99              0.336                                 ok            True                  False
  CTSH           86.96               23            1.28              0.46         50.68                50.98         0.520            pass              0.524             66.8                           0.690               -1.45             -0.224                                 ok            True                  False
  TMUS           80.00               15            2.07              2.81        192.22                36.70         0.504            pass              0.126             13.9                           0.242               -1.94             -0.225                                 ok            True                  False
   TXN           93.94               33            0.36              0.76        301.99                69.06         0.627            pass              0.861             90.9                           0.499                4.07              0.581                                 ok           False                  False
  TEAM           88.89               36            1.56              0.95         86.21               114.61         0.621            pass              0.680             69.3                           0.673               -3.98             -0.526 downtrend_blocked_slope_and_streak           False                  False
  PAYX           95.45               22            0.23              0.15         94.42                29.36         0.560            pass              0.815             92.9                           0.757                4.48              0.246                                 ok           False                  False
 GOOGL           88.89               36            0.54              1.48        387.03                41.27         0.497 below_threshold              0.627             55.7                           0.482               -3.14             -0.198                                 ok           False                  False
  AMGN           85.19               27            0.43              0.99        330.32                26.77         0.496 below_threshold              0.557             85.3                           0.563                0.21              0.010                                 ok           False                  False
  ADSK           88.46               26            1.15              1.96        243.32                38.52         0.494 below_threshold              0.605             74.5                           0.716               -0.71             -0.144                                 ok           False                  False
  GOOG           88.57               35            0.58              1.57        384.23                41.08         0.490 below_threshold              0.607             54.2                           0.455               -3.16             -0.208           downtrend_blocked_streak           False                  False
   KDP           90.00               40            0.14              0.03         28.84                34.80         0.487 below_threshold              0.793             92.4                           0.708                0.88              0.149                                 ok           False                  False
  SNPS           97.62               42            0.06              0.20        493.78                41.71         0.484 below_threshold              0.944             98.6                           0.854               -2.15             -0.333 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-20T11:20:04.061677-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:15:01.033814-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:10:02.083171-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:05:01.079772-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:00:03.973296-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T10:55:04.047991-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T10:50:01.057025-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T10:45:05.974600-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T10:40:03.515008-04:00 early_entry_1040 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T10:35:01.049335-04:00 early_entry_1035 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520112004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520112004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520112004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520112004)

</details>
