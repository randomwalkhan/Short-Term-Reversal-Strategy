# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 11:30:01 EDT`
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

- Cash: `$16,177.75`
- Equity: `$28,077.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$-240.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 11900.0        30.35          29.75      415.18        414.56          bid_ask_mid                      29.75                bid_ask_mid                    True          -240.0                  -1.98         91.67               36              0.62         50.17           49.73                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           95.00               20            0.88              0.64        103.85                32.97         0.582            pass              0.653             42.9                           0.466               -1.06             -0.044                                 ok            True                  False
  MELI           94.29               35            0.97             11.42       1673.00                61.16         0.575            pass              0.662             18.8                           0.217                1.78              0.499                                 ok            True                  False
  NVDA           87.88               33            0.71              1.08        219.05                44.83         0.505            pass              0.607             64.4                           0.733                1.28             -0.004                                 ok            True                  False
  INSM           72.00               25            2.23              1.71        108.80               111.27         0.730            pass              0.239             21.9                           0.410                5.66              0.005                                 ok           False                  False
  REGN           92.86               28            1.02              4.61        640.62                49.06         0.553            pass              0.744             75.2                           0.466              -10.90             -1.539 downtrend_blocked_slope_and_streak           False                  False
   WMT           91.30               23            0.78              0.67        121.05                34.61         0.542            pass              0.625             60.9                           0.748               -7.70             -0.493            downtrend_blocked_slope           False                  False
  COST           80.00                5            1.98             14.55       1044.21                22.19         0.530            pass              0.105             17.4                           0.365                2.07              0.545                                 ok           False                  False
 GOOGL           90.70               43            0.18              0.49        387.45                41.05         0.504            pass              0.779             81.0                           0.619               -3.45             -0.236                                 ok           False                  False
  GOOG           88.64               44            0.08              0.21        383.38                40.91         0.503            pass              0.752             90.5                           0.649               -3.50             -0.260 downtrend_blocked_slope_and_streak           False                  False
  MSTR           91.43               35            1.82              2.10        163.95                63.46         0.488 below_threshold              0.655             45.0                           0.540              -13.72             -1.836            downtrend_blocked_slope           False                  False
  PYPL           88.89               45            0.03              0.01         44.30                33.02         0.463 below_threshold              0.758             91.4                           0.577               -2.39             -0.308 downtrend_blocked_slope_and_streak           False                  False
  ISRG           87.18               39            0.57              1.74        439.05                36.27         0.463 below_threshold              0.583             50.6                           0.489               -2.83              0.206                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                     detail
2026-05-22T11:30:01.234875-04:00 early_entry_1130 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:25:01.413702-04:00 early_entry_1125 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:20:06.369988-04:00 early_entry_1120 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:15:01.374453-04:00 early_entry_1115 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:10:05.341387-04:00 early_entry_1110 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:05:02.181086-04:00 early_entry_1105 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:00:04.339955-04:00 early_entry_1100 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:55:05.343225-04:00 early_entry_1055 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:50:02.365980-04:00 early_entry_1050 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:45:01.349621-04:00 early_entry_1045 entry_skipped {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522113001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522113001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522113001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522113001)

</details>
