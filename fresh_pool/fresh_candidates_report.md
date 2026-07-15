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
1. `AKUN-001-UNKNOWN-VLESS-WS-59MS` (url=215ms, nekobox=242ms, status=yes)
2. `AKUN-002-ZOOM-VLESS-WS-61MS` (url=225ms, nekobox=241ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-73MS` (url=212ms, nekobox=239ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=222ms, nekobox=244ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-61MS` (url=218ms, nekobox=239ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-74MS` (url=207ms, nekobox=242ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-102MS` (url=213ms, nekobox=262ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-125MS` (url=220ms, nekobox=261ms, status=yes)
9. `AKUN-009-PUBLICDOMAINREGISTRY-NET-VLESS-WS-123MS` (url=218ms, nekobox=236ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS` (url=222ms, nekobox=7177ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-73MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-139MS` (url=232ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-126MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-128MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-WEBEX-VLESS-WS-104MS` (url=225ms, status=HTTP 204)
16. `AKUN-016-NEXUSMODS-VLESS-WS-96MS` (url=226ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-87MS` (url=216ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-153MS` (url=222ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-70MS` (url=222ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-78MS` (url=210ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-113MS` (url=218ms, status=HTTP 204)
22. `AKUN-022-US-VLESS-WS-112MS` (url=209ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-115MS` (url=230ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-340MS` (url=730ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-346MS` (url=729ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
