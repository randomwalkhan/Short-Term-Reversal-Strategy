# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-18 11:46:30 EDT`
Last processed slot: `early_entry_1145`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
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

- Cash: `$24,658.00`
- Equity: `$51,538.00`
- Realized PnL: `$36,898.00`
- Unrealized PnL: `$4,640.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ALNY     option         option ALNY260918C00220000       2026-08-17                   1     16     22240.0                 26880.0         13.9           16.8      224.68        228.33          bid_ask_mid                       16.8                bid_ask_mid                    True          4640.0                  20.86         84.62               26              1.73         43.62           44.92                 127.87                 332.0           21.0               0.06                      ok
```

## Today's Closed Trades (2026-08-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  UPRO           82.35               17            1.69              1.82        153.62                41.29         0.582            pass              0.226             19.4                           0.394               -1.52              0.007                                 ok            True                  False
  NVDA           86.36               22            2.24              3.53        223.50                39.09         0.503            pass              0.361             20.3                           0.582                3.79              0.316                                 ok            True                  False
   BKR           83.87               31            0.76              0.35         64.75                32.24         0.500 below_threshold              0.361             22.7                           0.317                4.72              0.576                                 ok            True                  False
  INSM           87.50               48            0.27              0.24        128.22               109.50         0.737            pass              0.719             81.9                           0.816               29.59              1.826                                 ok           False                  False
  SHOP           97.62               42            0.32              0.34        148.51                85.84         0.685            pass              0.921             84.3                           0.524               20.17              1.117                                 ok           False                  False
   APP           74.47               47            0.02              0.04        311.96                90.76         0.667            pass              0.563             98.7                           0.798              -25.68             -2.870            downtrend_blocked_slope           False                  False
  AMZN           83.72               43            0.28              0.50        261.09                61.74         0.607            pass              0.600             79.9                           0.578               -6.07             -0.666 downtrend_blocked_slope_and_streak           False                  False
  PCAR          100.00               11            1.84              1.69        130.12                28.21         0.562            pass              0.494             10.2                           0.290               -5.29             -0.393            downtrend_blocked_slope           False                  False
   HON           90.00               30            0.44              0.71        229.15                37.29         0.555            pass              0.567             37.3                           0.242               -7.90             -0.862            downtrend_blocked_slope           False                  False
  CSCO           77.78               18            1.60              1.26        112.36                42.21         0.547            pass              0.195             28.9                           0.542               -8.74             -1.021            downtrend_blocked_slope           False                  False
  GOOG           78.26               46            0.20              0.48        341.24                46.40         0.519            pass              0.499             82.4                           0.578               -9.22             -0.838            downtrend_blocked_slope           False                  False
 GOOGL           76.09               46            0.26              0.63        343.73                47.98         0.519            pass              0.481             76.4                           0.592               -9.15             -0.815            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-18T11:46:30.861767-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:55:01.557589-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:35:03.185404-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:33:08.530330-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T09:38:41.008763-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T09:20:07.104993-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T09:15:08.426968-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T09:11:00.046303-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T08:52:52.256088-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T08:35:07.917262-04:00     data_refresh       data_refresh                                                         {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260818114630)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260818114630)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260818114630)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260818114630)

</details>
