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
1. `AKUN-001-UNKNOWN-VLESS-WS-79MS` (url=201ms, nekobox=253ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-83MS` (url=226ms, nekobox=229ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-78MS` (url=227ms, nekobox=251ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-89MS` (url=201ms, nekobox=237ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-92MS` (url=225ms, nekobox=245ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-84MS` (url=223ms, nekobox=251ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-92MS` (url=218ms, nekobox=260ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-93MS` (url=231ms, nekobox=239ms, status=yes)
9. `AKUN-009-MYBB-VLESS-WS-89MS` (url=209ms, nekobox=247ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-94MS` (url=214ms, nekobox=259ms, status=yes)
11. `AKUN-011-HETZNER-VLESS-WS-98MS` (url=200ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-100MS` (url=288ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-102MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-85MS` (url=232ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-93MS` (url=209ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-99MS` (url=228ms, status=HTTP 204)
17. `AKUN-017-IDC-SG-VLESS-WS-101MS` (url=219ms, status=HTTP 204)
18. `AKUN-018-ES-FORNEX-20160629-VLESS-WS-99MS` (url=209ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-94MS` (url=205ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-112MS` (url=212ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-118MS` (url=228ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-84MS` (url=205ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-106MS` (url=207ms, status=HTTP 204)
24. `AKUN-024-VOV-VLESS-WS-111MS` (url=284ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-79MS` (url=222ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
