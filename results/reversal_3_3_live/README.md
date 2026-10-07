# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-07 14:15:04 EDT`
Last processed slot: `manual`

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

- Cash: `$53,034.30`
- Equity: `$107,209.30`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$2,062.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   1     55     52112.5                 54175.0         9.48           9.85      160.14        160.64          bid_ask_mid                       9.85                bid_ask_mid                    True          2062.5                   3.96         83.33               12               2.4         42.26           43.34                  40.56                 310.0           20.0               0.06                      ok
```

## Today's Closed Trades (2026-10-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           80.00               25            4.39              5.04        162.10               111.15         0.619            pass              0.294             43.9                           0.558                7.39              1.261                                 ok            True                  False
   KDP           93.33               15            1.24              0.27         31.01                26.61         0.540            pass              0.465              7.2                           0.232               -2.49             -0.206                                 ok            True                  False
  MPWR           82.35               17            3.03             31.30       1460.28                53.62         0.532            pass              0.243             26.7                           0.501                5.58              0.952                                 ok            True                  False
  NVDA           90.91               22            0.98              1.65        238.53                24.15         0.513            pass              0.468             15.2                           0.227                5.05              0.671                                 ok            True                  False
  UPRO           82.76               29            0.70              0.76        156.08                30.90         0.507            pass              0.453             67.5                           0.647                3.34              0.356                                 ok            True                  False
   MAR           84.21               19            0.97              2.45        360.23                17.15         0.500 below_threshold              0.333             36.9                           0.449                1.74              0.192                                 ok            True                  False
  DASH           82.14               28            1.62              2.20        192.68                42.81         0.500            pass              0.320             30.8                           0.523                0.64              0.205                                 ok            True                  False
  META           61.54               13            1.87              9.67        734.73                55.45         0.597            pass              0.153             24.6                           0.367               -2.56             -0.324            downtrend_blocked_slope           False                  False
   STX           88.89               36            0.35              1.99        804.78                69.91         0.581            pass              0.734             88.5                           0.747              -13.04             -1.269            downtrend_blocked_slope           False                  False
  QCOM           80.00               20            2.57              3.25        179.64                56.22         0.543            pass              0.175             18.1                           0.372              -10.58             -1.102 downtrend_blocked_slope_and_streak           False                  False
   CEG           86.84               38            0.40              0.85        300.04                58.89         0.537            pass              0.697             91.3                           0.823               13.38              1.078                                 ok           False                  False
   WDC           80.00               30            1.54              4.44        409.14                66.20         0.533            pass              0.351             54.7                           0.595              -14.57             -1.280            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-10-07T12:00:04.521112-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:55:05.517664-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:50:05.710520-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:45:01.712221-04:00 early_entry_1145 early_entry_shadow      {"contract_symbol": "FTNT261120C00190000", "current_drop_pct": 0.59, "early_entry_score": 0.723, "early_reclaim_pct": 65.3, "entry_ask": 16.2, "entry_bid": 14.2, "entry_mode": "early", "entry_option_price": 15.2, "hypothetical_budget": 26517.15, "hypothetical_contracts": 17, "matched_signals": 42, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 13.16, "option_volume": 11.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.68, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.723, "early_reclaim_pct": 65.3, "matched_signals": 42, "recovery_stability_score": 0.68, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-07T11:40:04.680085-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:35:06.426609-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:30:05.653907-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:25:06.559799-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:20:05.827676-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:15:06.288558-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "FTNT261120C00190000", "current_drop_pct": 0.62, "early_entry_score": 0.716, "early_reclaim_pct": 63.1, "entry_ask": 15.75, "entry_bid": 14.2, "entry_mode": "early", "entry_option_price": 14.975, "hypothetical_budget": 26517.15, "hypothetical_contracts": 17, "matched_signals": 42, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 10.35, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.724, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.476, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.716, "early_reclaim_pct": 63.1, "matched_signals": 42, "recovery_stability_score": 0.724, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.476, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261007141504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261007141504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261007141504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261007141504)

</details>
