# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-12 10:40:05 EDT`
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

- Cash: `$58,874.30`
- Equity: `$120,474.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$3,200.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH261120C00060000       2026-10-09                   1    160     58400.0                 61600.0         3.65           3.85       59.31         59.56          bid_ask_mid                       3.85                bid_ask_mid                    True          3200.0                   5.48          93.1               29              1.17         50.42           51.22                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           93.10               29            1.88              3.08        232.41                75.53         0.530            pass              0.594             21.6                           0.319               15.02              1.661                                 ok            True                  False
  SNPS           77.27               22            1.33              4.74        507.96                55.08         0.606            pass              0.181             13.3                           0.229               20.50              2.037                                 ok           False                  False
  QCOM           86.96               23            1.34              1.65        174.79                55.68         0.601            pass              0.420             29.3                           0.432               -7.65             -0.727 downtrend_blocked_slope_and_streak           False                  False
   STX           85.71               21            3.25             17.79        775.38                69.65         0.536            pass              0.293              4.6                           0.136              -17.79             -2.260            downtrend_blocked_slope           False                  False
 CMCSA           88.89               18            0.31              0.05         20.64                20.79         0.530            pass              0.522             59.4                           0.432               -4.02             -0.357            downtrend_blocked_slope           False                  False
   WDC           73.08               26            2.51              6.99        394.28                64.73         0.513            pass              0.182              7.9                           0.162              -14.55             -1.839            downtrend_blocked_slope           False                  False
  DASH           76.92               13            2.60              3.57        194.97                43.05         0.512            pass              0.159             29.2                           0.486                7.29              0.726                                 ok           False                  False
  INTC           77.78               18            3.40              2.49        103.63                69.66         0.509            pass              0.127              7.7                           0.209              -12.83             -1.471 downtrend_blocked_slope_and_streak           False                  False
  ABNB           89.19               37            0.56              0.65        165.59                38.25         0.499 below_threshold              0.677             67.4                           0.736                5.67              0.485                                 ok           False                   True
  UPRO           86.49               37            0.24              0.27        155.61                29.53         0.490 below_threshold              0.495             30.9                           0.283                4.43              0.617                                 ok           False                  False
  CSCO           33.33                3            2.90              2.41        117.36                33.46         0.482 below_threshold              0.055              2.1                           0.082                8.11              1.118                                 ok           False                  False
  ALNY           78.12               32            1.38              2.25        231.72                44.87         0.481 below_threshold              0.247             17.4                           0.220              -10.14             -1.100 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-10-12T10:40:05.705407-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "ADI261120C00420000", "current_drop_pct": 0.59, "early_entry_score": 0.782, "early_reclaim_pct": 66.9, "entry_ask": 14.3, "entry_bid": 12.9, "entry_mode": "early", "entry_option_price": 13.6, "hypothetical_budget": 29437.15, "hypothetical_contracts": 21, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 271.0, "option_spread_pct": 10.29, "option_volume": 54.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.782, "shadow_only": true, "success_rate": 94.12, "ticker": "ADI", "timing_score": 0.445, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.782, "early_reclaim_pct": 66.9, "matched_signals": 34, "recovery_stability_score": 0.782, "success_rate": 94.12, "ticker": "ADI", "timing_score": 0.445, "trend_health_status": "ok"}, {"current_drop_pct": 0.56, "early_entry_score": 0.677, "early_reclaim_pct": 67.4, "matched_signals": 37, "recovery_stability_score": 0.736, "success_rate": 89.19, "ticker": "ABNB", "timing_score": 0.499, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-12T10:35:03.248275-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:30:04.278592-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:25:04.307064-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:20:06.400928-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:15:06.352070-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:10:05.611490-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:05:03.362660-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T10:00:05.612405-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T03:00:05.508504-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 90, 'empty': 3}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261012104005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261012104005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261012104005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261012104005)

</details>
