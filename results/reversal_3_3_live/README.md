# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 10:35:01 EDT`
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

- Cash: `$2,162.75`
- Equity: `$31,782.75`
- Realized PnL: `$20,637.75`
- Unrealized PnL: `$1,145.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TTWO     option         option TTWO260717C00230000       2026-05-26                   0     15     14700.0                 15750.0         9.80          10.50      225.59        224.97          bid_ask_mid                      10.50                bid_ask_mid                    True          1050.0                   7.14        100.00               35              0.86         35.64           39.39                  35.40                 169.0           22.0               0.12                      ok
  SBUX     option         option SBUX260717C00105000       2026-05-22                   1     38     13775.0                 13870.0         3.62           3.65      103.16        101.25          bid_ask_mid                       3.65                bid_ask_mid                    True            95.0                   0.69         94.74               19              0.93         28.13           36.72                  32.97                2147.0           78.0               0.07                      ok
```

## Today's Closed Trades (2026-05-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AVGO     option         option AVGO260717C00420000      4          2026-05-21         2026-05-26        30.35       36.15 2320.0   19.110379 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  TEAM           90.48               42            0.76              0.46         85.22               109.49         0.676          pass              0.790             81.0                           0.605               -2.91              0.044                      ok            True                   True
  FTNT          100.00               42            0.60              0.56        133.69                66.43         0.579          pass              0.909             83.8                           0.653               15.32              1.651                      ok            True                   True
  MELI           91.67               24            1.98             23.02       1654.55                60.80         0.570          pass              0.556             31.4                           0.392                4.77              0.676                      ok            True                  False
   ADP          100.00               11            2.37              3.73        223.71                37.70         0.557          pass              0.480              6.0                           0.181                3.93              0.641                      ok            True                  False
  CTSH           86.36               22            1.36              0.50         52.53                46.65         0.543          pass              0.473             56.4                           0.608                6.39              1.328                      ok            True                  False
  AMGN           83.33               24            0.71              1.68        338.58                27.24         0.528          pass              0.235              0.0                           0.183                2.99              0.223                      ok            True                  False
 CMCSA           85.71               14            1.27              0.22         25.11                20.74         0.526          pass              0.295             21.0                           0.191               -0.58              0.014                      ok            True                  False
  CHTR           84.62               26            1.53              1.55        144.48                56.19         0.522          pass              0.312             10.1                           0.230               -3.29             -0.140                      ok            True                  False
  ROST           93.55               31            0.75              1.24        234.28                38.50         0.512          pass              0.707             51.6                           0.568                8.62              0.758                      ok            True                  False
   ROP           88.24               17            1.76              4.03        325.21                26.18         0.508          pass              0.344              8.9                           0.146               -2.32              0.045                      ok            True                  False
  INTU           80.00               20            2.76              6.19        317.29                90.56         0.651          pass              0.194             20.6                           0.254              -20.90             -2.243 downtrend_blocked_slope           False                  False
   TRI           77.78               18            0.87              0.52         85.64                55.00         0.638          pass              0.319             67.4                           0.728               -3.89              0.126                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-05-26T10:35:01.414005-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:30:01.317125-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:25:03.305112-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:20:01.300698-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:15:02.302661-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:10:01.332535-04:00 early_entry_1010                   entry {"allocated_cash": 14700.0, "asset_type": "option", "contract_symbol": "TTWO260717C00230000", "contracts": 15, "early_entry_score": 0.809, "entry_mode": "early", "entry_option_price": 9.8, "execution_mode": "option", "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 169.0, "option_spread_pct": 12.24, "option_volume": 22.0, "success_rate": 100.0, "ticker": "TTWO", "timing_score": 0.397}
2026-05-26T10:10:01.332535-04:00 early_entry_1010 entry_candidate_skipped                                                                                                                                                             {"early_entry_score": 0.848, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 53.06, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.615}
2026-05-26T10:05:02.315056-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-26T10:05:02.315056-04:00 early_entry_1005 entry_candidate_skipped                                                                                                                                                             {"early_entry_score": 0.842, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 50.98, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.611}
2026-05-26T10:05:02.315056-04:00      manage_1000                    exit                                                                                                                                                                                                                                            {"asset_type": "option", "contract_symbol": "AVGO260717C00420000", "fill_price": 36.15, "pnl": 2320.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 19.11, "ticker": "AVGO"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526103501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526103501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526103501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526103501)

</details>
