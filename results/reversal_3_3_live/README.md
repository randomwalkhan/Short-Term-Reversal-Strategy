# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 10:20:06 EST`
Last processed slot: `manage_1030`

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

- Cash: `$96,129.80`
- Equity: `$96,129.80`
- Realized PnL: `$86,129.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00380000     13          2026-11-19         2026-11-20        37.05      33.345 -4816.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MCHP           87.50               32            1.16              0.48         58.27                78.21         0.610          pass              0.585             59.3                           0.472               -0.96             -0.390                                 ok            True                  False
  INSM           84.44               45            0.57              0.58        144.21                87.95         0.533          pass              0.571             66.5                           0.334               25.54              1.889                                 ok            True                  False
  NXPI           93.33               30            1.19              2.10        250.86                49.35         0.512          pass              0.618             25.8                           0.243                0.19             -0.319                                 ok            True                  False
  INTC           65.52               29            2.04              0.80         55.38               141.91         0.783          pass              0.402             65.5                           0.467               -3.02             -0.853 downtrend_blocked_slope_and_streak           False                  False
   APP           85.71                7            4.97             13.19        373.37               122.37         0.724          pass              0.236              3.7                           0.198               -7.93             -0.671 downtrend_blocked_slope_and_streak           False                  False
  FTNT           70.00               20            2.39              2.20        130.52                96.17         0.675          pass              0.196             20.7                           0.268                7.98              0.686                                 ok           False                  False
   BKR           71.43               14            1.77              0.58         46.42                56.86         0.602          pass              0.189             34.2                           0.312               -3.77             -0.411 downtrend_blocked_slope_and_streak           False                  False
  QCOM           87.88               33            0.93              1.06        161.56                69.46         0.582          pass              0.624             67.3                           0.473               -2.97             -0.718 downtrend_blocked_slope_and_streak           False                  False
  UPRO           88.00               25            1.51              1.25        117.36                72.20         0.575          pass              0.546             58.3                           0.419               -9.95             -1.545 downtrend_blocked_slope_and_streak           False                  False
   ADI          100.00                5            4.01             10.60        372.90                64.58         0.568          pass              0.457              0.0                           0.265               -0.35             -0.434                                 ok           False                  False
  CSCO           73.08               26            1.00              0.67         94.42                50.60         0.543          pass              0.305             48.1                           0.384               -0.11             -0.355                                 ok           False                  False
   TXN           66.67                6            3.30              6.61        282.92                59.73         0.541          pass              0.093             13.1                           0.269               -0.38             -0.355                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-11-20T10:20:06.105218-05:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:20:06.105218-05:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"asset_type": "option", "contract_symbol": "APP270115C00380000", "fill_price": 33.345, "pnl": -4816.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "APP"}
2026-11-20T10:15:05.923687-05:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:10:04.986532-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:05:06.571641-05:00 early_entry_1005 early_entry_shadow   {"contract_symbol": "CEG270115C00250000", "current_drop_pct": 1.4, "early_entry_score": 0.698, "early_reclaim_pct": 63.5, "entry_ask": 17.2, "entry_bid": 15.0, "entry_mode": "early", "entry_option_price": 16.1, "hypothetical_budget": 26390.65, "hypothetical_contracts": 16, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 753.0, "option_spread_pct": 13.66, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.745, "shadow_only": true, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 1.4, "early_entry_score": 0.698, "early_reclaim_pct": 63.5, "matched_signals": 34, "recovery_stability_score": 0.745, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-20T10:00:05.975978-05:00 early_entry_1000 early_entry_shadow {"contract_symbol": "CEG270115C00250000", "current_drop_pct": 1.11, "early_entry_score": 0.722, "early_reclaim_pct": 71.0, "entry_ask": 18.0, "entry_bid": 16.0, "entry_mode": "early", "entry_option_price": 17.0, "hypothetical_budget": 26390.65, "hypothetical_contracts": 15, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 753.0, "option_spread_pct": 11.76, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.696, "shadow_only": true, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.511, "top_candidates": [{"current_drop_pct": 1.11, "early_entry_score": 0.722, "early_reclaim_pct": 71.0, "matched_signals": 34, "recovery_stability_score": 0.696, "success_rate": 91.18, "ticker": "CEG", "timing_score": 0.511, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-20T01:25:03.363046-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T01:20:04.815073-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T01:15:06.809821-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-20T01:10:05.934124-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120102006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120102006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120102006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120102006)

</details>
