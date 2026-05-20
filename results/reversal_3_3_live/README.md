# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 11:15:01 EDT`
Last processed slot: `early_entry_1115`

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
- Equity: `$27,547.75`
- Realized PnL: `$16,462.75`
- Unrealized PnL: `$1,085.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  FTNT     option         option FTNT260717C00125000       2026-05-20                   0     14     12355.0                 13440.0         8.82            9.6      126.75        128.47          bid_ask_mid                        9.6                bid_ask_mid                    True          1085.0                   8.78         100.0               38              0.69         41.39           39.71                  70.74                1300.0           40.0               0.12                      ok
```

## Today's Closed Trades (2026-05-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           90.91               11            1.34              1.26        133.66                20.68         0.536            pass              0.532             60.3                           0.611                1.98              0.335                                 ok            True                  False
  CTSH           86.96               23            1.28              0.46         50.68                50.98         0.520            pass              0.524             66.8                           0.701               -1.45             -0.224                                 ok            True                  False
 GOOGL           87.10               31            0.78              2.12        386.75                41.27         0.513            pass              0.490             36.3                           0.339               -3.37             -0.208                                 ok            True                  False
  TMUS           81.25               16            2.01              2.72        192.26                36.70         0.504            pass              0.174             16.7                           0.221               -1.87             -0.222                                 ok            True                  False
   TXN           93.94               33            0.25              0.54        302.08                69.06         0.634            pass              0.869             93.6                           0.451                4.18              0.586                                 ok           False                  False
  TEAM           89.74               39            1.18              0.72         86.31               114.61         0.627            pass              0.746             76.8                           0.734               -3.61             -0.508 downtrend_blocked_slope_and_streak           False                  False
  PAYX           95.45               22            0.29              0.19         94.40                29.36         0.556            pass              0.809             91.0                           0.744                4.42              0.243                                 ok           False                  False
   KDP           88.89               36            0.28              0.06         28.83                34.80         0.504            pass              0.715             84.8                           0.660                0.74              0.143                                 ok           False                  False
  GOOG           87.10               31            0.80              2.14        383.98                41.08         0.501            pass              0.492             37.4                           0.333               -3.37             -0.218           downtrend_blocked_streak           False                  False
  ADSK           88.46               26            1.12              1.91        243.34                38.52         0.495 below_threshold              0.607             75.1                           0.740               -0.68             -0.143                                 ok           False                  False
  AMGN           85.19               27            0.48              1.12        330.27                26.77         0.492 below_threshold              0.551             83.5                           0.514                0.16              0.008                                 ok           False                  False
   TRI           75.00               12            2.51              1.53         86.69                57.28         0.492 below_threshold              0.203             46.9                           0.293               -7.18             -0.896 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-20T11:15:01.033814-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:10:02.083171-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:05:01.079772-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T11:00:03.973296-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T10:55:04.047991-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T10:50:01.057025-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T10:45:05.974600-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T10:40:03.515008-04:00 early_entry_1040 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T10:35:01.049335-04:00 early_entry_1035 entry_skipped {"reason": "daily_entry_limit"}
2026-05-20T10:30:01.058983-04:00 early_entry_1030 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520111501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520111501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520111501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520111501)

</details>
