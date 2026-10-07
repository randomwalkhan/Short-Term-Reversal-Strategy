# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-07 13:00:05 EDT`
Last processed slot: `manage_1300`

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
- Equity: `$106,521.80`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$1,375.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   1     55     52112.5                 53487.5         9.48           9.72      160.14        160.48          bid_ask_mid                       9.72                bid_ask_mid                    True          1375.0                   2.64         83.33               12               2.4         42.26            43.6                  40.56                 310.0           20.0               0.06                      ok
```

## Today's Closed Trades (2026-10-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           85.00               20            1.53              3.22        299.02                58.89         0.578          pass              0.459             67.1                           0.663               12.09              1.026                                 ok            True                  False
   KDP           94.12               17            1.04              0.23         31.03                26.61         0.541          pass              0.521             14.5                           0.192               -2.30             -0.197                                 ok            True                  False
  SNPS           81.58               38            0.67              2.35        504.16                54.22         0.532          pass              0.419             45.5                           0.389               21.49              2.331                                 ok            True                  False
  MPWR           80.00               15            3.33             34.33       1458.98                53.62         0.525          pass              0.145             19.6                           0.400                5.26              0.939                                 ok            True                  False
  UPRO           82.61               23            1.13              1.24        155.88                30.90         0.519          pass              0.350             47.3                           0.533                2.89              0.337                                 ok            True                  False
  NVDA           91.30               23            0.96              1.61        238.55                24.15         0.509          pass              0.490             17.0                           0.211                5.07              0.672                                 ok            True                  False
  DASH           80.00               25            1.76              2.38        192.60                42.81         0.508          pass              0.226             25.0                           0.227                0.50              0.199                                 ok            True                  False
    ZS           93.62               47            0.15              0.22        212.16                73.32         0.611          pass              0.887             87.6                           0.770               -1.17              0.003                                 ok           False                  False
  SOXL           79.17               24            4.79              5.51        161.90               111.15         0.603          pass              0.270             38.7                           0.590                6.93              1.242                                 ok           False                  False
  META           61.54               13            1.90              9.83        734.67                55.45         0.595          pass              0.150             23.4                           0.360               -2.59             -0.325            downtrend_blocked_slope           False                  False
   STX           87.88               33            1.00              5.63        803.22                69.91         0.560          pass              0.622             67.5                           0.351              -13.60             -1.299            downtrend_blocked_slope           False                  False
  QCOM           83.33               24            2.12              2.68        179.88                56.22         0.553          pass              0.277             13.2                           0.410              -10.16             -1.081 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261007130005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261007130005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261007130005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261007130005)

</details>
