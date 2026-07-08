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
1. `AKUN-001-WPENG-VLESS-WS-94MS` (url=277ms, nekobox=304ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-103MS` (url=247ms, nekobox=320ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-114MS` (url=241ms, nekobox=277ms, status=yes)
4. `AKUN-004-ZOOM-VLESS-WS-112MS` (url=261ms, nekobox=288ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-101MS` (url=243ms, nekobox=290ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-122MS` (url=237ms, nekobox=340ms, status=yes)
7. `AKUN-007-ES-FORNEX-20160629-VLESS-WS-117MS` (url=243ms, nekobox=281ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-124MS` (url=252ms, nekobox=295ms, status=yes)
9. `AKUN-009-OVH-VLESS-WS-114MS` (url=272ms, nekobox=281ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-127MS` (url=284ms, nekobox=289ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-102MS` (url=291ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-121MS` (url=239ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-123MS` (url=285ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-139MS` (url=288ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-134MS` (url=262ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-140MS` (url=302ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-132MS` (url=237ms, status=HTTP 204)
18. `AKUN-018-DIGITALOCEAN-VLESS-WS-103MS` (url=237ms, status=HTTP 204)
19. `AKUN-019-U1HOST-FRA-VLESS-WS-112MS` (url=272ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-107MS` (url=261ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-135MS` (url=299ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-150MS` (url=346ms, status=HTTP 204)
23. `AKUN-023-WPENG-VLESS-WS-109MS` (url=260ms, status=HTTP 204)
24. `AKUN-024-NETCUP-VLESS-WS-129MS` (url=233ms, status=HTTP 204)
25. `AKUN-025-HOSTOFF-NET-VLESS-WS-123MS` (url=242ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
