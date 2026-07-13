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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-67MS` (url=211ms, nekobox=229ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-68MS` (url=211ms, nekobox=232ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-72MS` (url=212ms, nekobox=245ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-69MS` (url=219ms, nekobox=239ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-63MS` (url=207ms, nekobox=254ms, status=yes)
6. `AKUN-006-PUBLICDOMAINREGISTRY-NET-VLESS-WS-72MS` (url=210ms, nekobox=228ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS` (url=203ms, nekobox=260ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-81MS` (url=206ms, nekobox=261ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=225ms, nekobox=261ms, status=yes)
10. `AKUN-010-NET-82-21-84-0-24-VLESS-WS-97MS` (url=218ms, nekobox=268ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-92MS` (url=202ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-88MS` (url=230ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-113MS` (url=230ms, status=HTTP 204)
14. `AKUN-014-WEBEX-VLESS-WS-123MS` (url=204ms, status=HTTP 204)
15. `AKUN-015-SPEEDTEST-VLESS-WS-102MS` (url=216ms, status=HTTP 204)
16. `AKUN-016-US-VLESS-WS-92MS` (url=221ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-81MS` (url=227ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-105MS` (url=224ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-114MS` (url=200ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-126MS` (url=226ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-101MS` (url=213ms, status=HTTP 204)
22. `AKUN-022-POLICE-VLESS-WS-117MS` (url=263ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-128MS` (url=233ms, status=HTTP 204)
24. `AKUN-024-DPDNS-VLESS-WS-155MS` (url=224ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-241MS` (url=493ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
