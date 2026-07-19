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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-77MS` (url=205ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=199ms, nekobox=242ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-83MS` (url=231ms, nekobox=232ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS` (url=225ms, nekobox=230ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-86MS` (url=236ms, nekobox=240ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-104MS` (url=229ms, nekobox=228ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-94MS` (url=208ms, nekobox=262ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-110MS` (url=216ms, nekobox=257ms, status=yes)
9. `AKUN-009-UK-GB-DCL-01-20191003-VLESS-WS-89MS` (url=237ms, nekobox=232ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-97MS` (url=225ms, nekobox=239ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-98MS` (url=227ms, status=HTTP 204)
12. `AKUN-012-SAVVY-7-VLESS-WS-123MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-ZVC-VLESS-WS-93MS` (url=231ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-127MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-117MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-111MS` (url=222ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-125MS` (url=233ms, status=HTTP 204)
18. `AKUN-018-466688-VLESS-WS-137MS` (url=231ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-103MS` (url=223ms, status=HTTP 204)
20. `AKUN-020-UK-GB-DCL-01-20191003-VLESS-WS-148MS` (url=236ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-107MS` (url=243ms, status=HTTP 204)
22. `AKUN-022-UK-GB-DCL-01-20191003-VLESS-WS-115MS` (url=209ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-115MS` (url=218ms, status=HTTP 204)
24. `AKUN-024-WPENG-VLESS-WS-134MS` (url=273ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-145MS` (url=239ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
