# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 11:35:01 EDT`
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
- Equity: `$28,177.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$-140.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 12000.0        30.35           30.0      415.18        414.71          bid_ask_mid                       30.0                bid_ask_mid                    True          -140.0                  -1.15         91.67               36              0.62         50.17           50.32                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           94.12               17            0.97              0.71        103.83                32.97         0.596          pass              0.595             37.3                           0.374               -1.15             -0.048                                 ok            True                  False
  MELI           93.33               30            1.12             13.20       1672.24                61.16         0.596          pass              0.590             13.9                           0.239                1.62              0.492                                 ok            True                  False
  NVDA           87.88               33            0.71              1.09        219.04                44.83         0.504          pass              0.606             64.1                           0.740                1.28             -0.004                                 ok            True                  False
  INSM           72.00               25            1.96              1.51        108.88               111.27         0.744          pass              0.268             31.3                           0.490                5.95              0.018                                 ok           False                  False
  SHOP           84.09               44            0.03              0.02        104.85                78.48         0.618          pass              0.656             95.2                           0.671               -5.05              0.132                                 ok           False                  False
  REGN           92.00               25            1.18              5.30        640.32                49.06         0.562          pass              0.691             71.5                           0.463              -11.04             -1.546 downtrend_blocked_slope_and_streak           False                  False
  COST           80.00                5            1.92             14.12       1044.40                22.19         0.533          pass              0.113             19.9                           0.406                2.13              0.547                                 ok           False                  False
   WDC           95.12               41            0.38              1.31        485.90                59.01         0.530          pass              0.882             76.4                           0.446                0.96             -0.543                                 ok           False                  False
   WMT           92.59               27            0.69              0.59        121.09                34.61         0.523          pass              0.698             65.5                           0.777               -7.61             -0.489            downtrend_blocked_slope           False                  False
 GOOGL           90.48               42            0.22              0.59        387.41                41.05         0.508          pass              0.762             77.2                           0.559               -3.49             -0.238                                 ok           False                  False
  GOOG           88.64               44            0.10              0.28        383.35                40.91         0.501          pass              0.743             87.4                           0.591               -3.52             -0.261 downtrend_blocked_slope_and_streak           False                  False
  MSTR           90.32               31            2.03              2.34        163.85                63.46         0.500          pass              0.581             38.7                           0.507              -13.90             -1.846            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                     detail
2026-05-22T11:35:01.410809-04:00 early_entry_1135 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:30:01.234875-04:00 early_entry_1130 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:25:01.413702-04:00 early_entry_1125 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:20:06.369988-04:00 early_entry_1120 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:15:01.374453-04:00 early_entry_1115 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:10:05.341387-04:00 early_entry_1110 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:05:02.181086-04:00 early_entry_1105 entry_skipped {"reason": "no_candidate"}
2026-05-22T11:00:04.339955-04:00 early_entry_1100 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:55:05.343225-04:00 early_entry_1055 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:50:02.365980-04:00 early_entry_1050 entry_skipped {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522113501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522113501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522113501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522113501)

</details>
