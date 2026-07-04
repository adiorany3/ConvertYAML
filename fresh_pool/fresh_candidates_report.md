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
1. `AKUN-001-104-253-175-0-1-VLESS-WS-77MS` (url=219ms, nekobox=263ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-82MS` (url=232ms, nekobox=251ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-91MS` (url=230ms, nekobox=245ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-92MS` (url=207ms, nekobox=249ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-99MS` (url=242ms, nekobox=248ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-100MS` (url=204ms, nekobox=253ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-91MS` (url=219ms, nekobox=251ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS` (url=199ms, nekobox=258ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-113MS` (url=262ms, nekobox=235ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-115MS` (url=221ms, nekobox=240ms, status=yes)
11. `AKUN-011-MEDIUM-VLESS-WS-99MS` (url=208ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-112MS` (url=211ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-86MS` (url=207ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-104MS` (url=214ms, status=HTTP 204)
15. `AKUN-015-MYBB-VLESS-WS-90MS` (url=229ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-116MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-ZOOM-VLESS-WS-113MS` (url=226ms, status=HTTP 204)
18. `AKUN-018-WPENG-VLESS-WS-92MS` (url=225ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-96MS` (url=237ms, status=HTTP 204)
20. `AKUN-020-466688-VLESS-WS-141MS` (url=209ms, status=HTTP 204)
21. `AKUN-021-1PASSWORD-VLESS-WS-109MS` (url=200ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-92MS` (url=207ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-244MS` (url=500ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-261MS` (url=550ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-241MS` (url=508ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
