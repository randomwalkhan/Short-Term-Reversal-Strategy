# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-17 15:55:06 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$14,060.75`
- Equity: `$26,885.75`
- Realized PnL: `$17,898.25`
- Unrealized PnL: `$-1,012.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GOOG     option         option GOOG260724C00380000       2026-06-17                   0     15     13837.5                 12825.0         9.23           8.55      363.95        362.09          bid_ask_mid                       8.55                bid_ask_mid                    True         -1012.5                  -7.32          80.0               10              1.93         34.49           34.58                  27.92                 639.0          103.0               0.09                      ok
```

## Today's Closed Trades (2026-06-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  DRAM     option         option DRAM260717C00069000     17          2026-06-16         2026-06-17        7.425        8.55 1912.5   15.151515 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MCHP           96.30               27            1.12              0.75         95.31                60.62         0.610          pass              0.687             37.4                           0.200               -2.48              0.101                                 ok            True                  False
   TXN           92.00               25            1.09              2.33        304.71                52.85         0.589          pass              0.625             48.5                           0.335               -1.86              0.005                                 ok            True                  False
  FTNT           94.44               18            1.86              1.91        146.20                47.06         0.535          pass              0.638             48.8                           0.420               -3.07             -0.267                                 ok            True                  False
   MAR           96.15               26            0.85              2.37        398.09                27.71         0.527          pass              0.671             37.2                           0.337                5.04              0.368                                 ok            True                  False
   LIN           96.15               26            0.71              2.57        517.07                19.32         0.520          pass              0.696             45.8                           0.368                4.08              0.416                                 ok            True                  False
   ROP           83.33               12            2.16              5.10        335.14                28.84         0.509          pass              0.217             21.3                           0.297               -1.92             -0.029                                 ok            True                  False
    ZS           70.37               27            1.98              1.76        126.48               152.67         0.860          pass              0.302             34.3                           0.382               -7.19             -0.618 downtrend_blocked_slope_and_streak           False                  False
  QCOM           92.50               40            0.05              0.08        214.04                98.60         0.728          pass              0.882             92.1                           0.425              -10.83             -1.405            downtrend_blocked_slope           False                  False
   XEL          100.00                3            1.89              1.04         78.53                23.22         0.629          pass              0.494             10.2                           0.208                0.26              0.198                                 ok           False                  False
  INTU           57.14               14            4.06              7.98        277.57                99.11         0.615          pass              0.106              5.9                           0.169              -16.31             -1.627 downtrend_blocked_slope_and_streak           False                  False
  CSCO           84.62               13            1.79              1.49        118.93                42.56         0.609          pass              0.260             18.8                           0.254               -8.25             -0.809            downtrend_blocked_slope           False                  False
  MPWR           94.12               17            3.05             31.98       1485.07                71.82         0.605          pass              0.521             12.4                           0.212              -10.58             -0.657            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et       slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-17T15:10:05.396926-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T15:05:04.450318-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T15:00:06.393380-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T14:55:04.542004-04:00 entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-17T14:50:06.575124-04:00 entry_1500 entry_candidate_skipped                                                                                                                                                               {"early_entry_score": 0.711, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 67.0, "option_spread_pct": 30.66, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.589}
2026-06-17T14:50:06.575124-04:00 entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                 {"early_entry_score": 0.468, "error": "XEL: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "XEL", "timing_score": 0.64}
2026-06-17T14:50:06.575124-04:00 entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                              {"early_entry_score": 0.541, "error": "PAYX: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "PAYX", "timing_score": 0.608}
2026-06-17T14:50:06.575124-04:00 entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-17", "training_samples": 5231, "window": 5}
2026-06-17T14:50:06.575124-04:00 entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                  {"early_entry_score": 0.1, "error": "AEP: no call expiries found in the 21-40 trading-day window.", "reason": "no_trade_option_unavailable", "ticker": "AEP", "timing_score": 0.582}
2026-06-17T14:50:06.575124-04:00 entry_1500                   entry {"allocated_cash": 13837.5, "asset_type": "option", "contract_symbol": "GOOG260724C00380000", "contracts": 15, "early_entry_score": 0.146, "entry_mode": "regular", "entry_option_price": 9.225, "execution_mode": "option", "matched_signals": 10, "option_liquidity_status": "ok", "option_open_interest": 639.0, "option_spread_pct": 9.21, "option_volume": 103.0, "success_rate": 80.0, "ticker": "GOOG", "timing_score": 0.538}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260617155506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260617155506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260617155506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260617155506)

</details>
