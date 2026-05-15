# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 10:40:01 EDT`
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

- Cash: `$4,051.00`
- Equity: `$31,701.00`
- Realized PnL: `$21,986.00`
- Unrealized PnL: `$-285.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   0      5     14525.0                 15050.0        29.05           30.1      350.60        350.67          bid_ask_mid                       30.1                bid_ask_mid                    True           525.0                   3.61         97.30               37              0.63         45.67           46.82                  37.94                2023.0           40.0               0.13                      ok
  SNPS     option         option SNPS260618C00490000       2026-05-13                   2      3     13410.0                 12600.0        44.70           42.0      510.62        504.25          bid_ask_mid                       42.0                bid_ask_mid                    True          -810.0                  -6.04         97.14               35              0.50         52.16           56.25                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CDNS     option         option CDNS260618C00330000      5          2026-05-14         2026-05-15        32.35      29.115 -1617.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           80.00               30            1.06              2.18        293.23                90.16         0.724          pass              0.406             66.8                           0.735               -1.42              0.025                                 ok            True                  False
   TXN           92.00               25            1.02              2.20        307.23                67.99         0.688          pass              0.704             71.9                           0.731                9.10              1.061                                 ok            True                  False
  SNPS           96.88               32            1.13              4.04        508.29                41.57         0.542          pass              0.728             42.4                           0.314                3.11              0.317                                 ok            True                  False
 GOOGL           87.50               32            0.76              2.13        400.16                40.65         0.540          pass              0.594             64.5                           0.593                3.20              0.335                                 ok            True                  False
  GOOG           87.88               33            0.75              2.08        396.28                40.76         0.538          pass              0.606             63.0                           0.559                2.87              0.323                                 ok            True                  False
  MCHP           87.50               16            2.97              2.02         96.18                50.84         0.519          pass              0.347             18.4                           0.282                0.22             -0.091                                 ok            True                  False
  CDNS           97.30               37            0.74              1.82        352.06                37.94         0.515          pass              0.823             63.8                           0.618                2.73              0.198                                 ok            True                   True
  MDLZ           86.36               22            0.85              0.36         60.81                21.64         0.513          pass              0.301              0.0                           0.153               -1.50             -0.089                                 ok            True                  False
  CHTR           84.62               26            1.64              1.69        147.27               114.29         0.735          pass              0.499             65.2                           0.873              -15.23             -1.605            downtrend_blocked_slope           False                  False
  INSM           46.67               15            3.31              2.68        114.47               110.45         0.631          pass              0.141             14.7                           0.274              -16.11             -2.263 downtrend_blocked_slope_and_streak           False                  False
  INTC          100.00                7            5.49              4.46        114.02               111.79         0.599          pass              0.567             35.7                           0.564                9.98              1.686                                 ok           False                  False
  GEHC           64.29               28            1.31              0.57         62.42                57.53         0.582          pass              0.323             48.4                           0.365                1.34              0.218                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-05-15T10:40:01.261107-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-15T10:35:04.245705-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-15T10:30:01.313959-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-15T10:25:04.076553-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-15T10:20:01.244544-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-15T10:15:04.078787-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-15T10:10:04.236759-04:00 early_entry_1010         entry {"allocated_cash": 14525.0, "asset_type": "option", "contract_symbol": "CDNS260618C00330000", "contracts": 5, "early_entry_score": 0.838, "entry_mode": "early", "entry_option_price": 29.05, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 2023.0, "option_spread_pct": 13.43, "option_volume": 40.0, "success_rate": 97.3, "ticker": "CDNS", "timing_score": 0.521}
2026-05-15T10:10:04.236759-04:00      manage_1000          exit                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "CDNS260618C00330000", "fill_price": 29.115, "pnl": -1617.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CDNS"}
2026-05-15T10:05:04.229030-04:00 early_entry_1005 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "max_open_positions"}
2026-05-15T10:00:02.295451-04:00 early_entry_1000 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "max_open_positions"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515104001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515104001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515104001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515104001)

</details>
