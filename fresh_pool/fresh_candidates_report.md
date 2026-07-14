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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=211ms, nekobox=244ms, status=yes)
2. `AKUN-002-PUBLICDOMAINREGISTRY-NET-VLESS-WS-70MS` (url=200ms, nekobox=253ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-67MS` (url=199ms, nekobox=233ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-65MS` (url=209ms, nekobox=233ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-68MS` (url=213ms, nekobox=240ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-73MS` (url=209ms, nekobox=241ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-81MS` (url=218ms, nekobox=256ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-66MS` (url=249ms, nekobox=239ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=229ms, nekobox=240ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-103MS` (url=225ms, nekobox=239ms, status=yes)
11. `AKUN-011-SPEEDTEST-VLESS-WS-107MS` (url=234ms, status=HTTP 204)
12. `AKUN-012-POLICE-VLESS-WS-111MS` (url=226ms, status=HTTP 204)
13. `AKUN-013-US-VLESS-WS-81MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-110MS` (url=205ms, status=HTTP 204)
15. `AKUN-015-SPEEDTEST-VLESS-WS-106MS` (url=221ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-118MS` (url=231ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-123MS` (url=232ms, status=HTTP 204)
18. `AKUN-018-466688-VLESS-WS-122MS` (url=220ms, status=HTTP 204)
19. `AKUN-019-VOV-VLESS-WS-114MS` (url=246ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-120MS` (url=212ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-133MS` (url=216ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-129MS` (url=251ms, status=HTTP 204)
23. `AKUN-023-WEBEX-VLESS-WS-81MS` (url=210ms, status=HTTP 204)
24. `AKUN-024-SPEEDTEST-VLESS-WS-227MS` (url=638ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-252MS` (url=492ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
