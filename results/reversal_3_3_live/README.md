# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 10:05:06 EST`
Last processed slot: `manage_1000`

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

- Cash: `$52,781.30`
- Equity: `$96,461.30`
- Realized PnL: `$90,946.30`
- Unrealized PnL: `$-4,485.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   APP     option         option APP270115C00380000       2026-11-19                   1     13     48165.0                 43680.0        37.05           33.6      380.27        368.65          bid_ask_mid                       33.6                bid_ask_mid                    True         -4485.0                  -9.31         94.74               19              2.72          61.7           66.79                 121.61                 578.0           37.0                0.1                      ok
```

## Today's Closed Trades (2026-11-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FTNT           81.08               37            1.10              1.01        131.03                96.17         0.665          pass              0.466             63.6                           0.467                9.41              0.745                                 ok            True                  False
   TXN           84.62               13            1.94              3.88        284.09                59.73         0.610          pass              0.313             36.3                           0.581                1.02             -0.291                                 ok            True                  False
  MCHP           86.49               37            0.87              0.36         58.32                78.21         0.596          pass              0.621             69.5                           0.687               -0.67             -0.377                                 ok            True                  False
   ADI           80.00               15            2.17              5.74        374.98                64.58         0.594          pass              0.230             45.8                           0.594                1.56             -0.348                                 ok            True                  False
   APP           90.48               21            2.58              6.85        376.08               122.37         0.778          pass              0.553             40.7                           0.355               -5.62             -0.559 downtrend_blocked_slope_and_streak           False                  False
  SOXL           60.00               15            9.51              3.01         44.01               254.86         0.641          pass              0.193             31.7                           0.623              -10.83             -2.466            downtrend_blocked_slope           False                  False
   BKR           86.21               29            0.72              0.23         46.57                56.86         0.592          pass              0.571             73.3                           0.803               -2.74             -0.363 downtrend_blocked_slope_and_streak           False                  False
  ASML           75.00               12            2.60             24.73       1345.60                61.72         0.572          pass              0.165             31.5                           0.608               -7.29             -1.200 downtrend_blocked_slope_and_streak           False                  False
  QCOM           89.47               38            0.71              0.80        161.67                69.46         0.567          pass              0.722             75.2                           0.590               -2.75             -0.708 downtrend_blocked_slope_and_streak           False                  False
  MRVL           58.82               17            4.96              4.81        136.41               121.47         0.541          pass              0.186             28.6                           0.509               -6.80             -1.224            downtrend_blocked_slope           False                  False
  CSCO           81.08               37            0.17              0.11         94.65                50.60         0.537          pass              0.536             91.3                           0.809                0.74             -0.317                                 ok           False                  False
  MPWR           42.86               14            3.89             35.28       1280.74                90.01         0.537          pass              0.173             30.8                           0.626                4.62             -0.438                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-11-20T10:05:06.571641-05:00 early_entry_1005 early_entry_shadow   {"contract_symbol": "CEG270115C00250000", "current_drop_pct": 1.4, "early_entry_score": 0.698, "early_reclaim_pct": 63.5, "entry_ask": 17.2, "entry_bid": 15.0, "entry_mode": "early", "entry_option_price": 16.1, "hypothetical_budget": 26390.65, "hypothetical_contracts": 16, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 753.0, "option_spread_pct": 13.66, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.745, "shadow_only": true, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 1.4, "early_entry_score": 0.698, "early_reclaim_pct": 63.5, "matched_signals": 34, "recovery_stability_score": 0.745, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-20T10:00:05.975978-05:00 early_entry_1000 early_entry_shadow {"contract_symbol": "CEG270115C00250000", "current_drop_pct": 1.11, "early_entry_score": 0.722, "early_reclaim_pct": 71.0, "entry_ask": 18.0, "entry_bid": 16.0, "entry_mode": "early", "entry_option_price": 17.0, "hypothetical_budget": 26390.65, "hypothetical_contracts": 15, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 753.0, "option_spread_pct": 11.76, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.696, "shadow_only": true, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.511, "top_candidates": [{"current_drop_pct": 1.11, "early_entry_score": 0.722, "early_reclaim_pct": 71.0, "matched_signals": 34, "recovery_stability_score": 0.696, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.511, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-20T01:25:03.363046-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T01:20:04.815073-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T01:15:06.809821-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T01:10:05.934124-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T01:05:05.898904-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T01:00:05.809710-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T00:55:04.836951-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T00:50:02.820195-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120100506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120100506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120100506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120100506)

</details>
