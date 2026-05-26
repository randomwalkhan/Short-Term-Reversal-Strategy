# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 10:45:02 EDT`
Last processed slot: `early_entry_1045`

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

- Cash: `$2,162.75`
- Equity: `$32,127.75`
- Realized PnL: `$20,637.75`
- Unrealized PnL: `$1,490.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TTWO     option         option TTWO260717C00230000       2026-05-26                   0     15     14700.0                 16950.0         9.80          11.30      225.59        223.76          bid_ask_mid                      11.30                bid_ask_mid                    True          2250.0                  15.31        100.00               35              0.86         35.64           43.29                  35.40                 169.0           22.0               0.12                      ok
  SBUX     option         option SBUX260717C00105000       2026-05-22                   1     38     13775.0                 13015.0         3.62           3.42      103.16        101.64          bid_ask_mid                       3.42                bid_ask_mid                    True          -760.0                  -5.52         94.74               19              0.93         28.13           34.08                  32.97                2147.0           78.0               0.07                      ok
```

## Today's Closed Trades (2026-05-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AVGO     option         option AVGO260717C00420000      4          2026-05-21         2026-05-26        30.35       36.15 2320.0   19.110379 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           90.91               44            0.69              0.41         85.24               109.49         0.669          pass              0.806             82.8                           0.586               -2.84              0.048                                 ok            True                   True
  MELI           91.67               24            1.98             23.05       1654.54                60.80         0.570          pass              0.555             31.3                           0.365                4.76              0.676                                 ok            True                  False
   ADP           93.33               15            1.99              3.14        223.96                37.70         0.543          pass              0.506             20.9                           0.301                4.33              0.658                                 ok            True                  False
  CTSH           85.00               20            1.58              0.58         52.50                46.65         0.540          pass              0.402             49.4                           0.474                6.15              1.318                                 ok            True                  False
   ROP           88.89               18            1.59              3.64        325.38                26.18         0.513          pass              0.395             17.7                           0.178               -2.15              0.053                                 ok            True                  False
 CMCSA           80.00               15            1.23              0.22         25.11                20.74         0.513          pass              0.155             23.5                           0.154               -0.54              0.016                                 ok            True                  False
  INTU           80.00               20            2.79              6.26        317.26                90.56         0.649          pass              0.191             19.7                           0.183              -20.92             -2.245            downtrend_blocked_slope           False                  False
  CSCO           80.00                5            2.14              1.80        119.64                52.25         0.647          pass              0.132             22.4                           0.424               19.37              1.871                                 ok           False                  False
   TRI           73.33               15            1.19              0.71         85.55                55.00         0.632          pass              0.263             55.7                           0.453               -4.19              0.112                                 ok           False                  False
  SBUX           92.31               13            1.43              1.03        102.67                33.02         0.595          pass              0.516             36.2                           0.387               -3.31             -0.275            downtrend_blocked_slope           False                  False
   WMT           93.75               16            1.17              0.98        119.85                34.37         0.593          pass              0.503             12.2                           0.219               -6.84             -0.837 downtrend_blocked_slope_and_streak           False                  False
   AEP           78.95               19            0.33              0.31        131.46                25.20         0.591          pass              0.330             70.3                           0.507                0.34              0.072                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-05-26T10:45:02.313357-04:00 early_entry_1045           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:40:05.315818-04:00 early_entry_1040           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:35:01.414005-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:30:01.317125-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:25:03.305112-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:20:01.300698-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:15:02.302661-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:10:01.332535-04:00 early_entry_1010                   entry {"allocated_cash": 14700.0, "asset_type": "option", "contract_symbol": "TTWO260717C00230000", "contracts": 15, "early_entry_score": 0.809, "entry_mode": "early", "entry_option_price": 9.8, "execution_mode": "option", "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 169.0, "option_spread_pct": 12.24, "option_volume": 22.0, "success_rate": 100.0, "ticker": "TTWO", "timing_score": 0.397}
2026-05-26T10:10:01.332535-04:00 early_entry_1010 entry_candidate_skipped                                                                                                                                                             {"early_entry_score": 0.848, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 53.06, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.615}
2026-05-26T10:05:02.315056-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_trade_after_option_and_timing_filters"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526104502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526104502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526104502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526104502)

</details>
