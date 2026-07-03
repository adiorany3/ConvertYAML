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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-92MS` (url=207ms, nekobox=253ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-92MS` (url=219ms, nekobox=270ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-90MS` (url=205ms, nekobox=246ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-94MS` (url=204ms, nekobox=234ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-96MS` (url=227ms, nekobox=265ms, status=yes)
6. `AKUN-006-DIGITALOCEAN-VLESS-WS-110MS` (url=222ms, nekobox=260ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-116MS` (url=220ms, nekobox=246ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-123MS` (url=231ms, nekobox=267ms, status=yes)
9. `AKUN-009-COMPREND-NET-VLESS-WS-114MS` (url=204ms, nekobox=266ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-114MS` (url=219ms, nekobox=262ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-107MS` (url=218ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-126MS` (url=251ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-110MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-123MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-WEBEX-VLESS-WS-134MS` (url=226ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-107MS` (url=225ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-122MS` (url=213ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-119MS` (url=220ms, status=HTTP 204)
19. `AKUN-019-ADF-VLESS-WS-98MS` (url=215ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-370MS` (url=781ms, status=HTTP 204)
21. `AKUN-022-SPEEDTEST-VLESS-WS-370MS` (url=765ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-333MS` (url=579ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-398MS` (url=835ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-400MS` (url=780ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-406MS` (url=909ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
