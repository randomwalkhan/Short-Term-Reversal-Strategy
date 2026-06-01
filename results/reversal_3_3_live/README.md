# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 10:35:01 EDT`
Last processed slot: `manage_1030`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$16,749.25`
- Equity: `$31,289.25`
- Realized PnL: `$20,849.25`
- Unrealized PnL: `$440.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   1      4     14100.0                 14540.0        35.25          36.35      477.34        478.03          bid_ask_mid                      36.35                bid_ask_mid                    True           440.0                   3.12         97.22               36              0.69         45.69           52.63                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-06-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MRVL     option         option MRVL260717C00200000      5          2026-06-01         2026-06-01         28.3       25.47 -1415.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MELI           94.44               36            0.75              8.94       1691.82                60.97         0.597          pass              0.652             11.3                           0.116                8.80              0.826                                 ok            True                  False
  ROST           93.75               16            1.48              2.39        230.70                40.27         0.591          pass              0.572             35.3                           0.492                7.31              1.037                                 ok            True                  False
  LRCX           88.89               27            1.33              2.96        316.91                55.15         0.548          pass              0.592             62.2                           0.622               10.27              1.567                                 ok            True                  False
  AAPL           92.31               13            1.43              3.13        310.72                17.18         0.533          pass              0.402              0.1                           0.210                2.45              0.461                                 ok            True                  False
  KLAC           90.62               32            0.94             12.58       1916.32                50.27         0.523          pass              0.631             49.7                           0.316                5.64              1.058                                 ok            True                  False
  MDLZ           93.33               15            1.19              0.51         60.95                14.75         0.514          pass              0.490             16.7                           0.193                0.01              0.029                                 ok            True                  False
  FAST           93.33               15            1.43              0.44         44.01                16.05         0.501          pass              0.444              1.6                           0.111                0.72              0.188                                 ok            True                  False
  SOXL           93.55               31            0.41              0.64        224.07               138.67         0.769          pass              0.859             93.6                           0.959               36.09              4.522                                 ok           False                  False
  INSM           61.90               21            2.63              1.97        106.07               110.85         0.732          pass              0.147              0.0                           0.150               -4.62             -0.230                                 ok           False                  False
  ASML           94.74               38            0.27              3.03       1611.46                52.38         0.571          pass              0.892             84.9                           0.751                7.10              0.981                                 ok           False                  False
   AEP           66.67                6            1.56              1.38        126.08                24.34         0.563          pass              0.067              3.4                           0.221               -0.36             -0.051                                 ok           False                  False
   WMT           84.21               19            1.07              0.87        115.38                32.67         0.555          pass              0.256              9.5                           0.195              -12.89             -1.672 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-06-01T10:35:01.685578-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:30:02.004330-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:25:05.840855-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:25:05.840855-04:00      manage_1030                    exit                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "MRVL260717C00200000", "fill_price": 25.47, "pnl": -1415.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MRVL"}
2026-06-01T10:20:03.923727-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:15:04.991229-04:00 early_entry_1015                   entry {"allocated_cash": 14150.0, "asset_type": "option", "contract_symbol": "MRVL260717C00200000", "contracts": 5, "early_entry_score": 0.862, "entry_mode": "early", "entry_option_price": 28.3, "execution_mode": "option", "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 4958.0, "option_spread_pct": 5.3, "option_volume": 50.0, "success_rate": 100.0, "ticker": "MRVL", "timing_score": 0.526}
2026-06-01T10:10:06.342773-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate"}
2026-06-01T10:05:05.997517-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate"}
2026-06-01T10:00:03.895970-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-01T10:00:03.895970-04:00 early_entry_1000 entry_candidate_skipped                                                                                                                                          {"early_entry_score": 0.779, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 2.0, "option_spread_pct": null, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "MDLZ", "timing_score": 0.419}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601103501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601103501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601103501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601103501)

</details>
