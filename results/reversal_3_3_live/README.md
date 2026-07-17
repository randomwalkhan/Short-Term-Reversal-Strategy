# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-17 15:15:01 EDT`
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

- Cash: `$15,119.25`
- Equity: `$29,364.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$140.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   TXN     option         option TXN260821C00290000       2026-07-17                   0      7     14105.0                 14245.0        20.15          20.35      284.95        283.32          bid_ask_mid                      20.35                bid_ask_mid                    True           140.0                   0.99          90.0               20              2.15         62.88           65.49                  64.46                 207.0          231.0               0.09                      ok
```

## Today's Closed Trades (2026-07-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MDLZ          100.00               14            0.75              0.32         61.28                33.43         0.612          pass              0.610             40.6                           0.539                0.08              0.074                  ok            True                  False
   KHC           90.91               11            1.28              0.23         26.13                36.78         0.587          pass              0.411             18.3                           0.295                2.07              0.342                  ok            True                  False
   TXN           88.24               17            2.71              5.53        288.85                64.46         0.582          pass              0.427             34.0                           0.341               -3.33             -0.236                  ok            True                  False
   ADI           87.50               24            1.70              4.52        378.59                54.65         0.575          pass              0.510             53.1                           0.524               -0.82             -0.015                  ok            True                  False
   XEL          100.00               12            1.21              0.68         79.69                21.95         0.558          pass              0.543             24.6                           0.407               -3.59             -0.203                  ok            True                  False
  ASML           92.00               25            2.03             25.34       1774.01                64.12         0.555          pass              0.642             55.6                           0.336               -1.17             -0.063                  ok            True                  False
   WBD           83.33               12            1.17              0.22         27.19                20.20         0.534          pass              0.267             37.3                           0.490                1.85              0.466                  ok            True                  False
   CSX           87.50               16            0.92              0.33         50.75                21.08         0.530          pass              0.362             23.0                           0.312                3.13              0.394                  ok            True                  False
  NXPI           83.33               24            1.80              3.41        269.20                54.99         0.528          pass              0.415             59.9                           0.486               -2.77             -0.238                  ok            True                  False
   ADP           96.30               27            0.67              1.21        256.04                34.79         0.524          pass              0.764             66.2                           0.620                5.19              0.575                  ok            True                  False
  GILD           90.48               21            1.17              1.12        135.82                34.67         0.518          pass              0.456             17.1                           0.297                2.61              0.103                  ok            True                  False
  PAYX          100.00               31            0.58              0.46        114.50                35.43         0.504          pass              0.800             70.0                           0.619                7.23              0.759                  ok            True                   True
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-07-17T15:10:06.696610-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-17T15:05:06.030959-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-17T15:00:09.838561-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-17T14:55:11.420522-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-17T14:50:08.434742-04:00       entry_1500                   entry {"allocated_cash": 14105.0, "asset_type": "option", "contract_symbol": "TXN260821C00290000", "contracts": 7, "early_entry_score": 0.537, "entry_mode": "regular", "entry_option_price": 20.15, "execution_mode": "option", "matched_signals": 20, "option_liquidity_status": "ok", "option_open_interest": 207.0, "option_spread_pct": 8.93, "option_volume": 231.0, "success_rate": 90.0, "ticker": "TXN", "timing_score": 0.602}
2026-07-17T14:50:08.434742-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                         {"early_entry_score": 0.572, "option_liquidity_status": "low_volume", "option_open_interest": 709.0, "option_spread_pct": 11.11, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "MDLZ", "timing_score": 0.602}
2026-07-17T14:50:08.434742-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                       {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-17", "training_samples": 5456, "window": 5}
2026-07-17T12:00:05.871771-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:55:01.882856-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:50:01.906755-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260717151501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260717151501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260717151501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260717151501)

</details>
