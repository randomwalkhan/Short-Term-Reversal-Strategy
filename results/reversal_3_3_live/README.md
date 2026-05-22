# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 10:45:01 EDT`
Last processed slot: `early_entry_1045`

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
- Equity: `$28,307.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$-10.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 12130.0        30.35          30.33      415.18        411.91          bid_ask_mid                      30.33                bid_ask_mid                    True           -10.0                  -0.08         91.67               36              0.62         50.17           52.27                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           95.24               21            0.74              0.54        103.90                32.97         0.585          pass              0.688             52.2                           0.627               -0.92             -0.038                                 ok            True                  False
  NVDA           88.00               25            1.35              2.07        218.62                44.83         0.518          pass              0.461             32.1                           0.437                0.63             -0.033                                 ok            True                  False
  INSM           70.83               24            2.29              1.76        108.78               111.27         0.736          pass              0.167              0.0                           0.150                5.59              0.003                                 ok           False                  False
   TRI           82.61               23            0.31              0.19         85.48                54.99         0.605          pass              0.466             83.0                           0.348               -7.53             -0.288           downtrend_blocked_streak           False                  False
  MELI           94.87               39            0.47              5.48       1675.55                61.16         0.587          pass              0.761             37.5                           0.250                2.30              0.523                                 ok           False                  False
   WMT           90.00               10            1.48              1.26        120.80                34.61         0.584          pass              0.403             25.9                           0.410               -8.35             -0.525            downtrend_blocked_slope           False                  False
  REGN           93.10               29            0.98              4.42        640.69                49.06         0.549          pass              0.760             76.2                           0.466              -10.86             -1.537 downtrend_blocked_slope_and_streak           False                  False
  CHTR           78.95               19            2.17              2.26        147.93               115.38         0.525          pass              0.115              0.9                           0.185               -5.94             -0.363                                 ok           False                  False
  COST           75.00                4            2.19             16.08       1043.56                22.19         0.517          pass              0.075              7.7                           0.205                1.85              0.535                                 ok           False                  False
 GOOGL           90.70               43            0.15              0.41        387.48                41.05         0.506          pass              0.788             84.0                           0.806               -3.43             -0.235                                 ok           False                  False
  GOOG           88.64               44            0.05              0.14        383.41                40.91         0.504          pass              0.762             93.6                           0.837               -3.47             -0.259 downtrend_blocked_slope_and_streak           False                  False
  AVGO           91.89               37            0.55              1.60        413.88                40.36         0.503          pass              0.690             47.5                           0.396               -4.12             -0.386            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                     detail
2026-05-22T10:45:01.349621-04:00 early_entry_1045 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:40:01.398827-04:00 early_entry_1040 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:35:05.737690-04:00 early_entry_1035 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:30:05.162989-04:00 early_entry_1030 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:25:01.354544-04:00 early_entry_1025 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:20:04.321834-04:00 early_entry_1020 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:15:04.350743-04:00 early_entry_1015 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:10:01.349213-04:00 early_entry_1010 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:05:01.370986-04:00 early_entry_1005 entry_skipped {"reason": "no_candidate"}
2026-05-22T10:00:02.359616-04:00 early_entry_1000 entry_skipped {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522104501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522104501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522104501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522104501)

</details>
