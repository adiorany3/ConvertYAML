# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 18
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 24

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-ORACLE-VLESS-WS-73MS` (url=234ms, nekobox=312ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-81MS` (url=302ms, nekobox=270ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-70MS` (url=243ms, nekobox=271ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-93MS` (url=252ms, nekobox=262ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-105MS` (url=354ms, nekobox=285ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-92MS` (url=255ms, nekobox=269ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-85MS` (url=227ms, nekobox=307ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-101MS` (url=263ms, nekobox=268ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=249ms, nekobox=290ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-288MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-294MS` (url=650ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-312MS` (url=648ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-328MS` (url=5050ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-100MS` (url=303ms, status=HTTP 204)
15. `AKUN-019-CLOUDFLARE-VLESS-WS-419MS` (url=1050ms, status=HTTP 204)
16. `AKUN-023-CONFLU-VLESS-WS-284MS` (url=577ms, status=HTTP 204)
17. `AKUN-024-CLOUDFLARE-VLESS-WS-536MS` (url=800ms, status=HTTP 204)
18. `AKUN-032-UNKNOWN-VLESS-WS-624MS` (url=785ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
