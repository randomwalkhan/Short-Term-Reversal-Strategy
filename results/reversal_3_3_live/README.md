# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-12 11:05:41 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$58,874.30`
- Equity: `$116,474.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$-800.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH261120C00060000       2026-10-09                   1    160     58400.0                 57600.0         3.65            3.6       59.31         59.73          bid_ask_mid                        3.6                bid_ask_mid                    True          -800.0                  -1.37          93.1               29              1.17         50.42            51.0                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           88.89               27            1.00              2.09        297.18                62.49         0.551            pass              0.450             14.9                           0.166               13.31              1.721                                 ok            True                  False
    ZS           91.67               36            1.40              2.29        232.75                75.53         0.513            pass              0.661             41.7                           0.457               15.58              1.683                                 ok            True                  False
  ABNB           87.50               32            0.93              1.08        165.41                38.25         0.506            pass              0.536             46.3                           0.453                5.29              0.469                                 ok            True                  False
  MSTR           91.89               37            0.36              0.39        154.17                79.86         0.647            pass              0.766             68.2                           0.286               -2.14             -0.192                                 ok           False                  False
  SNPS           72.22               18            1.78              6.34        507.27                55.08         0.595            pass              0.136              7.8                           0.175               19.95              2.016                                 ok           False                  False
  QCOM           88.46               26            1.19              1.47        174.87                55.68         0.593            pass              0.503             37.3                           0.627               -7.51             -0.720 downtrend_blocked_slope_and_streak           False                  False
   STX           83.33               24            2.98             16.36        775.99                69.65         0.530            pass              0.272             12.2                           0.330              -17.57             -2.248            downtrend_blocked_slope           False                  False
 CMCSA           89.47               19            0.27              0.04         20.64                20.79         0.528            pass              0.562             65.6                           0.451               -3.97             -0.355            downtrend_blocked_slope           False                  False
   WDC           75.86               29            2.03              5.64        394.86                64.73         0.526            pass              0.256             25.6                           0.490              -14.12             -1.816            downtrend_blocked_slope           False                  False
  INTC           81.25               16            3.58              2.62        103.58                69.66         0.514            pass              0.133              2.6                           0.192              -13.00             -1.480 downtrend_blocked_slope_and_streak           False                  False
  DASH           76.92               13            2.65              3.65        194.94                43.05         0.508            pass              0.154             27.6                           0.430                7.23              0.724                                 ok           False                  False
  UPRO           84.21               38            0.09              0.10        155.68                29.53         0.492 below_threshold              0.572             74.5                           0.597                4.59              0.624                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-10-12T11:05:41.766229-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "TXN261120C00280000", "current_drop_pct": 0.58, "early_entry_score": 0.708, "early_reclaim_pct": 75.5, "entry_ask": 18.3, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 17.8, "hypothetical_budget": 29437.15, "hypothetical_contracts": 16, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 390.0, "option_spread_pct": 5.62, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.783, "shadow_only": true, "success_rate": 89.47, "ticker": "TXN", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.708, "early_reclaim_pct": 75.5, "matched_signals": 38, "recovery_stability_score": 0.783, "success_rate": 89.47, "ticker": "TXN", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-12T10:55:05.736003-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:50:05.423702-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:45:04.583763-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:40:05.705407-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "ADI261120C00420000", "current_drop_pct": 0.59, "early_entry_score": 0.782, "early_reclaim_pct": 66.9, "entry_ask": 14.3, "entry_bid": 12.9, "entry_mode": "early", "entry_option_price": 13.6, "hypothetical_budget": 29437.15, "hypothetical_contracts": 21, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 271.0, "option_spread_pct": 10.29, "option_volume": 54.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.782, "shadow_only": true, "success_rate": 94.12, "ticker": "ADI", "timing_score": 0.445, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.782, "early_reclaim_pct": 66.9, "matched_signals": 34, "recovery_stability_score": 0.782, "success_rate": 94.12, "ticker": "ADI", "timing_score": 0.445, "trend_health_status": "ok"}, {"current_drop_pct": 0.56, "early_entry_score": 0.677, "early_reclaim_pct": 67.4, "matched_signals": 37, "recovery_stability_score": 0.736, "success_rate": 89.19, "ticker": "ABNB", "timing_score": 0.499, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-12T10:35:03.248275-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:30:04.278592-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:25:04.307064-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:20:06.400928-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:15:06.352070-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261012110541)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261012110541)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261012110541)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261012110541)

</details>
