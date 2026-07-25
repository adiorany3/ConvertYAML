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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=202ms, nekobox=227ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-55MS` (url=204ms, nekobox=227ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=197ms, nekobox=224ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=201ms, nekobox=227ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-59MS` (url=210ms, nekobox=232ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-86MS` (url=200ms, nekobox=226ms, status=yes)
7. `AKUN-007-DEV-VLESS-WS-73MS` (url=200ms, nekobox=231ms, status=yes)
8. `AKUN-008-008500-VLESS-WS-72MS` (url=208ms, nekobox=230ms, status=yes)
9. `AKUN-009-OVH-VLESS-WS-79MS` (url=222ms, nekobox=230ms, status=yes)
10. `AKUN-010-SPEEDTEST-VLESS-WS-91MS` (url=211ms, nekobox=170ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-106MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-75MS` (url=202ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-82MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-101MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-89MS` (url=206ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-109MS` (url=207ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-113MS` (url=210ms, status=HTTP 204)
18. `AKUN-018-ZVC-VLESS-WS-67MS` (url=212ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-142MS` (url=242ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-87MS` (url=221ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-139MS` (url=204ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-72MS` (url=204ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-108MS` (url=204ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-213MS` (url=509ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-220MS` (url=540ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
