# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-07 10:10:02 EDT`
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

- Cash: `$53,034.30`
- Equity: `$103,359.30`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$-1,787.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   1     55     52112.5                 50325.0         9.48           9.15      160.14        159.18          bid_ask_mid                       9.15                bid_ask_mid                    True         -1787.5                  -3.43         83.33               12               2.4         42.26           44.82                  40.56                 310.0           20.0               0.06                      ok
```

## Today's Closed Trades (2026-10-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           92.50               40            0.57              0.85        211.89                73.32         0.629          pass              0.722             41.8                           0.250               -1.59             -0.016                                 ok            True                  False
  SNPS           80.00               30            0.99              3.51        503.67                54.22         0.561          pass              0.211              7.1                           0.085               21.09              2.316                                 ok            True                  False
  UPRO           91.67               12            1.96              2.15        155.49                30.90         0.550          pass              0.382              1.0                           0.090                2.02              0.298                                 ok            True                  False
   KDP           95.00               20            0.93              0.20         31.04                26.61         0.534          pass              0.520              0.0                           0.033               -2.19             -0.192                                 ok            True                  False
  CRWD           80.00               20            2.76              5.38        276.55                55.11         0.525          pass              0.192             24.2                           0.257                3.31              0.706                                 ok            True                  False
  MPWR           80.00               15            3.41             35.18       1458.61                53.62         0.521          pass              0.138             17.6                           0.199                5.17              0.935                                 ok            True                  False
  DASH           80.00               25            1.77              2.39        192.59                42.81         0.512          pass              0.177              8.6                           0.185                0.49              0.198                                 ok            True                  False
  SHOP           86.49               37            1.05              1.20        163.92                52.70         0.501          pass              0.534             43.8                           0.598               14.32              1.480                                 ok            True                  False
  META           58.33               12            2.12             10.94        734.19                55.45         0.586          pass              0.096              7.9                           0.172               -2.80             -0.335            downtrend_blocked_slope           False                  False
  QCOM           87.50               32            0.90              1.14        180.54                56.22         0.580          pass              0.586             60.6                           0.655               -9.05             -1.025 downtrend_blocked_slope_and_streak           False                  False
   CEG           85.71                7            2.98              6.26        297.72                58.89         0.577          pass              0.318             36.1                           0.588               10.45              0.959                                 ok           False                  False
   STX           88.24               34            0.94              5.30        803.36                69.91         0.559          pass              0.644             69.4                           0.673              -13.55             -1.296            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-07T10:10:02.695128-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:05:05.843456-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:00:06.491610-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T00:00:06.148407-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 92, 'empty': 1}
2026-10-06T15:10:04.494335-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-06T15:05:04.280902-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-06T15:00:04.457281-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-06T14:55:01.305987-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-06T14:50:04.366747-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-06", "training_samples": 5941, "window": 5}
2026-10-06T14:50:04.366747-04:00       entry_1500              entry {"allocated_cash": 52112.5, "asset_type": "option", "contract_symbol": "ABNB261120C00160000", "contracts": 55, "early_entry_score": 0.219, "entry_mode": "regular", "entry_option_price": 9.475, "execution_mode": "option", "matched_signals": 12, "option_liquidity_status": "ok", "option_open_interest": 310.0, "option_spread_pct": 5.8, "option_volume": 20.0, "success_rate": 83.33, "ticker": "ABNB", "timing_score": 0.529}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261007101002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261007101002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261007101002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261007101002)

</details>
