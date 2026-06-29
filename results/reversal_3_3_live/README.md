# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-29 15:40:05 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$14,720.50`
- Equity: `$28,720.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$-640.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260821C00130000       2026-06-29                   0     32     14640.0                 14000.0         4.58           4.38      126.19        125.83          bid_ask_mid                       4.38                bid_ask_mid                    True          -640.0                  -4.37         93.33               15              1.32         33.41           32.45                  29.34                 807.0           40.0               0.08                      ok
```

## Today's Closed Trades (2026-06-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   XEL          100.00               20            0.54              0.31         82.10                23.26         0.591          pass              0.645             39.8                           0.388                4.02              0.528                      ok            True                  False
  GILD           91.67               12            1.61              1.44        127.26                29.34         0.564          pass              0.422             13.8                           0.237                0.84              0.073                      ok            True                  False
  SBUX           88.46               26            0.60              0.44        104.41                26.41         0.524          pass              0.549             54.7                           0.360                0.91              0.257                      ok            True                  False
  PAYX          100.00               27            0.59              0.41         99.72                33.42         0.523          pass              0.749             61.3                           0.374               -1.31             -0.221                      ok            True                  False
   HON            0.00                1            5.58              9.51        239.33               250.29         0.995          pass              0.104              1.5                           0.156                4.32              5.924                      ok           False                  False
  DRAM           92.86               28            0.13              0.06         71.85               125.47         0.847          pass              0.842             98.3                           0.834               10.43              0.728                      ok           False                  False
  MPWR           91.18               34            0.36              3.33       1311.89                89.21         0.659          pass              0.785             87.2                           0.404              -17.04             -1.898 downtrend_blocked_slope           False                  False
   TXN           94.12               34            0.20              0.39        285.26                70.58         0.635          pass              0.883             94.2                           0.527               -5.40             -0.584 downtrend_blocked_slope           False                  False
  QCOM           91.43               35            0.24              0.32        189.25                89.86         0.626          pass              0.810             92.1                           0.479              -10.76             -1.426 downtrend_blocked_slope           False                  False
  NXPI           94.12               34            0.33              0.64        276.74                66.10         0.604          pass              0.863             88.7                           0.556               -9.13             -0.988 downtrend_blocked_slope           False                  False
   EXC           78.57               14            0.83              0.28         47.28                19.58         0.570          pass              0.164             26.9                           0.431                1.72              0.250                      ok           False                  False
  CDNS           92.59               27            1.30              3.44        375.79                56.11         0.564          pass              0.555             16.6                           0.312               -3.28             -0.557 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-29T15:10:05.899695-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T15:05:05.773719-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T15:00:06.338367-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T14:55:08.793154-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-29T14:50:09.505108-04:00       entry_1500                   entry {"allocated_cash": 14640.0, "asset_type": "option", "contract_symbol": "GILD260821C00130000", "contracts": 32, "early_entry_score": 0.533, "entry_mode": "regular", "entry_option_price": 4.575, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 807.0, "option_spread_pct": 7.65, "option_volume": 40.0, "success_rate": 93.33, "ticker": "GILD", "timing_score": 0.563}
2026-06-29T14:50:09.505108-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                {"early_entry_score": 0.248, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 22.22, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "EXC", "timing_score": 0.577}
2026-06-29T14:50:09.505108-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-29", "training_samples": 5314, "window": 5}
2026-06-29T12:00:02.850105-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:55:01.636700-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:50:05.501340-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260629154005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260629154005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260629154005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260629154005)

</details>
