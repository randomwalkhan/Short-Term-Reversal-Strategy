# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-25 14:20:05 EDT`
Last processed slot: `manage_1430`

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

- Cash: `$2,402.75`
- Equity: `$28,422.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$105.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SBUX     option         option SBUX260717C00105000       2026-05-22                   0     38     13775.0                 14060.0         3.62            3.7      103.16        102.83          bid_ask_mid                        3.7                bid_ask_mid                    True           285.0                   2.07         94.74               19              0.93         28.13           29.98                  32.97                2147.0           78.0               0.07                      ok
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 11960.0        30.35           29.9      415.18        412.85          bid_ask_mid                       29.9                bid_ask_mid                    True          -180.0                  -1.48         91.67               36              0.62         50.17           51.25                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-25)

_None_

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et        slot    event_type                                                     detail
2026-05-25T14:20:05.027407-04:00 manage_1430 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T14:15:04.968995-04:00      manual market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T14:10:05.148132-04:00 manage_1400  slot_skipped                            {"reason": "already_processed"}
2026-05-25T14:05:02.982359-04:00 manage_1400  slot_skipped                            {"reason": "already_processed"}
2026-05-25T14:00:06.042079-04:00 manage_1400  slot_skipped                            {"reason": "already_processed"}
2026-05-25T13:55:06.016226-04:00 manage_1400  slot_skipped                            {"reason": "already_processed"}
2026-05-25T13:50:04.955795-04:00 manage_1400 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T13:45:04.980342-04:00      manual market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T13:40:05.010678-04:00 manage_1330  slot_skipped                            {"reason": "already_processed"}
2026-05-25T13:35:06.407405-04:00 manage_1330  slot_skipped                            {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260525142005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260525142005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260525142005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260525142005)

</details>
