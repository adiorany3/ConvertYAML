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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS` (url=200ms, nekobox=225ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-56MS` (url=214ms, nekobox=233ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-64MS` (url=198ms, nekobox=229ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS` (url=197ms, nekobox=236ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-55MS` (url=210ms, nekobox=226ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-83MS` (url=208ms, nekobox=224ms, status=yes)
7. `AKUN-007-SM-VLESS-WS-74MS` (url=207ms, nekobox=227ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-92MS` (url=199ms, nekobox=173ms, status=no)
9. `AKUN-008-UNKNOWN-VLESS-WS-80MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-107MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-113MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-105MS` (url=220ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-104MS` (url=210ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-116MS` (url=314ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-138MS` (url=223ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-113MS` (url=222ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-61MS` (url=259ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-384MS` (url=654ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-399MS` (url=405ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-222MS` (url=472ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-404MS` (url=814ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-500MS` (url=837ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-504MS` (url=784ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-414MS` (url=713ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-503MS` (url=813ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
