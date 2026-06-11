# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-11 14:10:04 EDT`
Last processed slot: `manage_1400`

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

- Cash: `$28,725.75`
- Equity: `$28,725.75`
- Realized PnL: `$18,725.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-11)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CTSH     option         option CTSH260717C00055000     73          2026-06-09         2026-06-11         2.05       1.845 -1496.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PAYX          100.00               22            0.56              0.40        100.93                34.22         0.578            pass              0.767             76.3                           0.732                5.26              0.311                                 ok            True                  False
  CDNS           94.44               36            0.63              1.69        384.40                58.86         0.536            pass              0.840             76.1                           0.440                2.37             -0.127                                 ok            True                  False
  WDAY           84.21               19            2.98              2.87        136.24                67.65         0.513            pass              0.354             43.6                           0.646                2.58             -0.500                                 ok            True                  False
  INTU           73.91               23            2.08              4.13        282.45               101.53         0.704            pass              0.295             46.1                           0.542              -11.08             -1.741 downtrend_blocked_slope_and_streak           False                  False
   TRI           82.61               23            0.83              0.48         81.76                68.04         0.661            pass              0.441             72.9                           0.694               -3.80             -0.773 downtrend_blocked_slope_and_streak           False                  False
  MSFT           50.00                6            2.18              6.08        394.76                36.94         0.526            pass              0.158             35.0                           0.424               -8.97             -1.392 downtrend_blocked_slope_and_streak           False                  False
  CTSH           89.66               29            0.91              0.33         51.67                46.99         0.521            pass              0.670             78.0                           0.725               -4.66             -0.771 downtrend_blocked_slope_and_streak           False                  False
  TEAM           88.46               26            3.11              1.99         90.69                86.53         0.506            pass              0.513             43.3                           0.693               -4.93             -1.560 downtrend_blocked_slope_and_streak           False                  False
   ADP           97.44               39            0.30              0.48        230.89                32.69         0.485 below_threshold              0.896             84.8                           0.769                4.80              0.332                                 ok           False                  False
  MDLZ           93.10               29            0.64              0.29         64.06                18.57         0.474 below_threshold              0.643             39.7                           0.311                2.21              0.383                                 ok           False                  False
  META           75.86               29            0.90              3.58        569.44                37.32         0.472 below_threshold              0.364             63.3                           0.609              -10.93             -1.054 downtrend_blocked_slope_and_streak           False                  False
  SNPS           81.82               22            2.01              6.49        457.76                48.54         0.468 below_threshold              0.296             40.3                           0.314               -6.11             -0.750            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-06-11T11:58:26.585033-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-11T11:22:14.657857-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "KDP260717C00031000", "current_drop_pct": 0.74, "early_entry_score": 0.82, "early_reclaim_pct": 76.7, "entry_ask": 1.45, "entry_bid": 1.1, "entry_mode": "early", "entry_option_price": 1.275, "hypothetical_budget": 14362.88, "hypothetical_contracts": 112, "matched_signals": 32, "option_liquidity_status": "wide_spread", "option_open_interest": 2194.0, "option_spread_pct": 27.45, "option_volume": 80.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 96.88, "ticker": "KDP", "timing_score": 0.433, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.82, "early_reclaim_pct": 76.7, "matched_signals": 32, "recovery_stability_score": 0.703, "success_rate": 96.88, "ticker": "KDP", "timing_score": 0.433, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-11T10:46:23.679160-04:00 early_entry_1045 early_entry_shadow                         {"contract_symbol": "CSCO260717C00120000", "current_drop_pct": 0.61, "early_entry_score": 0.808, "early_reclaim_pct": 68.3, "entry_ask": 4.8, "entry_bid": 4.55, "entry_mode": "early", "entry_option_price": 4.675, "hypothetical_budget": 14362.88, "hypothetical_contracts": 30, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 11268.0, "option_spread_pct": 5.35, "option_volume": 155.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.626, "shadow_only": true, "success_rate": 96.77, "ticker": "CSCO", "timing_score": 0.631, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.808, "early_reclaim_pct": 68.3, "matched_signals": 31, "recovery_stability_score": 0.626, "success_rate": 96.77, "ticker": "CSCO", "timing_score": 0.631, "trend_health_status": "ok"}, {"current_drop_pct": 0.87, "early_entry_score": 0.795, "early_reclaim_pct": 72.8, "matched_signals": 30, "recovery_stability_score": 0.78, "success_rate": 96.67, "ticker": "KDP", "timing_score": 0.438, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-11T10:10:05.812920-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.68, "early_entry_score": 0.811, "early_reclaim_pct": 65.2, "entry_ask": 8.7, "entry_bid": 6.2, "entry_mode": "early", "entry_option_price": 7.45, "hypothetical_budget": 14362.88, "hypothetical_contracts": 19, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 261.0, "option_spread_pct": 33.56, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.682, "shadow_only": true, "success_rate": 97.14, "ticker": "ADP", "timing_score": 0.488, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.811, "early_reclaim_pct": 65.2, "matched_signals": 35, "recovery_stability_score": 0.682, "success_rate": 97.14, "ticker": "ADP", "timing_score": 0.488, "trend_health_status": "ok"}, {"current_drop_pct": 0.55, "early_entry_score": 0.778, "early_reclaim_pct": 70.9, "matched_signals": 39, "recovery_stability_score": 0.672, "success_rate": 92.31, "ticker": "ROP", "timing_score": 0.435, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-11T10:10:05.812920-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"asset_type": "option", "contract_symbol": "CTSH260717C00055000", "fill_price": 1.845, "pnl": -1496.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CTSH"}
2026-06-11T05:50:04.507646-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
2026-06-11T05:45:04.534672-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
2026-06-11T05:43:14.603904-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
2026-06-11T05:25:01.583807-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
2026-06-11T05:20:01.619276-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260611141004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260611141004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260611141004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260611141004)

</details>
