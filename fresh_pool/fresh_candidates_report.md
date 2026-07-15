# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=214ms, nekobox=250ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS` (url=215ms, nekobox=241ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-60MS` (url=227ms, nekobox=245ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-60MS` (url=222ms, nekobox=251ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-71MS` (url=205ms, nekobox=328ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-74MS` (url=221ms, nekobox=262ms, status=yes)
7. `AKUN-007-HETZNER-VLESS-WS-83MS` (url=209ms, nekobox=244ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-73MS` (url=200ms, nekobox=261ms, status=yes)
9. `AKUN-009-VULTR-VLESS-WS-79MS` (url=218ms, nekobox=241ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-83MS` (url=227ms, nekobox=239ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-84MS` (url=208ms, status=HTTP 204)
12. `AKUN-012-ADF-VLESS-WS-70MS` (url=206ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-82MS` (url=234ms, status=HTTP 204)
14. `AKUN-014-MEDIUM-VLESS-WS-97MS` (url=204ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-91MS` (url=206ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-73MS` (url=197ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-133MS` (url=239ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-62MS` (url=226ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-115MS` (url=247ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-79MS` (url=220ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-105MS` (url=202ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-102MS` (url=233ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-219MS` (url=424ms, status=HTTP 204)
24. `AKUN-024-ES-FORNEX-20160629-VLESS-WS-114MS` (url=204ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-86MS` (url=225ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
