# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-14 15:45:06 EDT`
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

- Cash: `$68,187.30`
- Equity: `$134,887.30`
- Realized PnL: `$125,462.30`
- Unrealized PnL: `$-575.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CSCO     option         option CSCO261120C00115000       2026-10-14                   0    115     67275.0                 66700.0         5.85            5.8       113.6        113.33          bid_ask_mid                        5.8                bid_ask_mid                    True          -575.0                  -0.85         86.67               15              1.28         44.93           45.64                  34.22                4547.0          159.0               0.02                      ok
```

## Today's Closed Trades (2026-10-14)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS261120C00500000     28          2026-10-13         2026-10-14         25.4       22.86 -7112.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           85.71               14            1.46              1.18        114.57                34.22         0.539            pass              0.256              7.7                           0.254                5.76              0.613                                 ok            True                  False
    ZS           84.62               13            3.16              5.05        226.49                58.33         0.523            pass              0.212              5.5                           0.195               11.04              1.649                                 ok            True                  False
  MSFT          100.00               11            1.78              6.79        540.54                20.68         0.522            pass              0.492             11.1                           0.342                4.07              0.536                                 ok            True                  False
  SNPS           71.43                7            3.21             11.12        489.74                50.26         0.550            pass              0.087             10.6                           0.220               10.04              0.599                                 ok           False                  False
  META           57.14                7            3.35             17.90        754.83                53.30         0.537            pass              0.082              9.4                           0.313                1.62              0.227                                 ok           False                  False
  MELI           72.73               11            2.43             31.91       1862.37                40.00         0.534            pass              0.126             22.0                           0.445                5.90              0.976                                 ok           False                  False
  QCOM           80.00               20            2.39              2.95        175.59                53.60         0.531            pass              0.203             27.7                           0.556               -6.19             -0.635 downtrend_blocked_slope_and_streak           False                  False
  SHOP           73.33               15            2.67              3.30        175.11                46.81         0.505            pass              0.160             25.2                           0.447               15.85              1.862                                 ok           False                  False
  INTC           85.71               14            4.02              2.89        101.57                67.54         0.502            pass              0.288             19.6                           0.495              -17.92             -2.140 downtrend_blocked_slope_and_streak           False                  False
  CDNS           77.78               18            1.84              4.31        332.35                36.71         0.501            pass              0.183             26.4                           0.430               -0.65             -0.259                                 ok           False                  False
  UPRO          100.00                2            3.58              3.90        153.73                28.27         0.494 below_threshold              0.504             18.3                           0.451                1.95              0.355                                 ok           False                  False
  TEAM          100.00               32            1.46              2.12        207.13                43.11         0.484 below_threshold              0.711             38.6                           0.595               14.34              1.350                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-10-14T15:10:06.171047-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-10-14T15:05:05.885010-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-10-14T15:00:05.913118-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-10-14T14:55:05.778063-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-10-14T14:50:04.996677-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"allocated_cash": 67275.0, "asset_type": "option", "contract_symbol": "CSCO261120C00115000", "contracts": 115, "early_entry_score": 0.292, "entry_mode": "regular", "entry_option_price": 5.85, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 4547.0, "option_spread_pct": 1.71, "option_volume": 159.0, "success_rate": 86.67, "ticker": "CSCO", "timing_score": 0.547}
2026-10-14T14:50:04.996677-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-14", "training_samples": 6059, "window": 5}
2026-10-14T12:00:05.972511-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:55:04.759815-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "PYPL261120C00055000", "current_drop_pct": 0.51, "early_entry_score": 0.838, "early_reclaim_pct": 64.2, "entry_ask": 3.65, "entry_bid": 3.5, "entry_mode": "early", "entry_option_price": 3.575, "hypothetical_budget": 67731.15, "hypothetical_contracts": 189, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 9142.0, "option_spread_pct": 4.2, "option_volume": 152.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.597, "shadow_only": true, "success_rate": 95.0, "ticker": "PYPL", "timing_score": 0.452, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.838, "early_reclaim_pct": 64.2, "matched_signals": 40, "recovery_stability_score": 0.597, "success_rate": 95.0, "ticker": "PYPL", "timing_score": 0.452, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-14T11:50:06.783855-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:45:05.905160-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261014154506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261014154506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261014154506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261014154506)

</details>
