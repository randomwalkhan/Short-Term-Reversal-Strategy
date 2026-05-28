# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 10:35:04 EDT`
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

- Cash: `$17,884.25`
- Equity: `$30,714.25`
- Realized PnL: `$20,384.25`
- Unrealized PnL: `$330.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-28                   0      4     12500.0                 12830.0        31.25          32.08      419.65        418.54          bid_ask_mid                      32.08                bid_ask_mid                    True           330.0                   2.64         89.19               37              0.52         51.04           52.34                  36.99                2631.0           27.0               0.06                      ok
```

## Today's Closed Trades (2026-05-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS260717C00500000      2          2026-05-27         2026-05-28        60.05      54.045 -1201.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           90.00               30            0.51              0.77        217.65               139.87         0.724            pass              0.760             95.8                           0.918               17.71              2.744                                 ok            True                   True
  CSCO           92.31               26            0.85              0.71        119.36                51.65         0.617            pass              0.618             40.3                           0.391               16.47              0.869                                 ok            True                  False
   XEL           95.24               21            1.02              0.58         80.75                25.49         0.547            pass              0.562             11.2                           0.207                0.33              0.230                                 ok            True                  False
  INTC           94.44               18            3.70              3.16        120.42                92.16         0.538            pass              0.546             18.0                           0.189               -2.52              0.657                                 ok            True                  False
  LRCX           86.67               30            1.01              2.25        317.96                56.04         0.534            pass              0.570             68.4                           0.799                6.86              1.138                                 ok            True                  False
   LIN           83.33               12            1.58              5.63        505.46                20.85         0.514            pass              0.194             13.5                           0.233               -2.62             -0.061                                 ok            True                  False
    ZS           85.19               27            1.77              1.57        125.74               152.21         0.826            pass              0.470             45.2                           0.662              -18.54             -1.215            downtrend_blocked_slope           False                  False
  MELI           95.12               41            0.22              2.56       1695.07                61.41         0.613            pass              0.889             75.9                           0.494                8.36              0.867                                 ok           False                  False
  ROST           88.89                9            2.08              3.40        232.01                38.54         0.586            pass              0.361             21.9                           0.375                7.96              1.157                                 ok           False                  False
   AEP           70.00               10            1.23              1.12        129.09                25.33         0.555            pass              0.217             54.0                           0.276                0.02              0.210                                 ok           False                  False
  REGN           88.24               34            0.53              2.32        626.75                48.81         0.529            pass              0.567             44.7                           0.449              -13.13             -1.305 downtrend_blocked_slope_and_streak           False                  False
  MPWR           92.59               27            1.42             16.08       1613.28                53.62         0.497 below_threshold              0.646             49.1                           0.653               -3.22              0.235           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-05-28T10:35:04.979836-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-28T10:30:05.932623-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-28T10:25:06.392243-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-28T10:20:03.857163-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-28T10:15:02.929662-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-28T10:10:02.928305-04:00 early_entry_1010 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-28T10:05:05.949315-04:00 early_entry_1005         entry {"allocated_cash": 12500.0, "asset_type": "option", "contract_symbol": "AVGO260717C00420000", "contracts": 4, "early_entry_score": 0.738, "entry_mode": "early", "entry_option_price": 31.25, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 2631.0, "option_spread_pct": 5.76, "option_volume": 27.0, "success_rate": 89.19, "ticker": "AVGO", "timing_score": 0.427}
2026-05-28T10:05:05.949315-04:00      manage_1000          exit                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "SNPS260717C00500000", "fill_price": 54.045, "pnl": -1201.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-05-28T10:00:04.925583-04:00 early_entry_1000 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-28T00:00:03.757313-04:00     data_refresh  data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 92}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528103504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528103504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528103504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528103504)

</details>
