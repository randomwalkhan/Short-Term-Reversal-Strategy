# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 11:40:05 EDT`
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

- Cash: `$19,575.25`
- Equity: `$31,435.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$-150.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 11860.0        60.05           59.3       531.8        526.02          bid_ask_mid                       59.3                bid_ask_mid                    True          -150.0                  -1.25         97.22               36              0.52         54.56           58.46                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           85.71               28            1.15              2.68        331.52                92.16         0.651            pass              0.444             35.6                           0.391               11.76              1.204                                 ok            True                  False
  ASML           91.30               23            2.36             26.99       1620.46                54.27         0.511            pass              0.503             21.4                           0.298                4.77              0.561                                 ok            True                  False
  UPRO           94.12               34            0.56              0.57        145.61                30.88         0.503            pass              0.625             12.8                           0.180                3.95              0.273                                 ok            True                  False
  INSM           70.37               27            2.24              1.71        108.14               110.60         0.714            pass              0.185              0.0                           0.170               -8.25             -0.902            downtrend_blocked_slope           False                  False
   AEP           80.00               20            0.32              0.29        130.78                25.21         0.595            pass              0.343             72.3                           0.723               -1.10              0.167                                 ok           False                  False
  REGN           86.67               30            0.89              3.96        632.92                48.91         0.581            pass              0.493             41.2                           0.349              -12.93             -1.495 downtrend_blocked_slope_and_streak           False                  False
  INTC           92.31               13            4.52              3.91        121.84                91.80         0.549            pass              0.444             13.5                           0.247               -2.22              0.327           downtrend_blocked_streak           False                  False
  FTNT          100.00                3            5.12              4.80        131.90                66.88         0.540            pass              0.495             13.8                           0.143               11.62              1.349                                 ok           False                  False
  ISRG           90.00               10            2.61              7.97        433.23                35.34         0.527            pass              0.326              2.1                           0.109               -1.53              0.127           downtrend_blocked_streak           False                  False
  NVDA           75.00               12            2.51              3.78        213.24                40.94         0.502            pass              0.097             11.2                           0.334               -5.13             -0.710 downtrend_blocked_slope_and_streak           False                  False
  MSTR           83.87               31            2.14              2.39        158.90                64.17         0.489 below_threshold              0.400             35.8                           0.578              -15.13             -1.701            downtrend_blocked_slope           False                  False
  MSFT           85.71               28            0.71              2.07        415.14                23.55         0.487 below_threshold              0.483             54.1                           0.426                1.52              0.225                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-27T11:40:05.644907-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:35:01.763028-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:30:03.642153-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:25:02.657208-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:20:01.673157-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:15:01.657140-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:10:01.701881-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:05:03.689642-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:00:02.698480-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T10:55:01.700501-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527114005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527114005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527114005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527114005)

</details>
